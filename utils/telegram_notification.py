from utils.timezone_utils import now_central
import os
import requests
import logging
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logger
logger = logging.getLogger(__name__)

class TelegramNotifier:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        
    def send_message(self, chat_id: str, message: str, parse_mode: str = "HTML") -> Dict[str, Any]:
        """
        Send a message to a Telegram chat
        
        Args:
            chat_id: Telegram chat ID
            message: Message text to send
            parse_mode: Message format (HTML or Markdown)
            
        Returns:
            Response from Telegram API
        """
        if not self.bot_token:
            return {"success": False, "error": "Telegram bot token not configured"}
            
        if not chat_id:
            return {"success": False, "error": "Chat ID not provided"}
            
        try:
            url = f"{self.base_url}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': message,
                'parse_mode': parse_mode,
                'disable_web_page_preview': True
            }
            
            response = requests.post(url, json=payload, timeout=10)
            result = response.json()
            
            if result.get("ok"):
                return {"success": True, "message_id": result.get("result", {}).get("message_id")}
            else:
                logger.error("Failed to send Telegram message: %s", result.get("description"))
                return {"success": False, "error": result.get("description", "Unknown error")}
                
        except Exception as e:
            logger.exception("Error sending Telegram message: %s", e)
            return {"success": False, "error": str(e)}
    
    def send_emergency_alert(
        self, 
        emergency: Dict[str, Any], 
        user_name: str
    ) -> Dict[str, Any]:
        """
        Send an emergency alert to Telegram using the severity computed by
        _local_emergency_detection in CompanionAgent.
        
        Args:
            emergency: Emergency detection result from CompanionAgent
            user_name: Name of the patient
            
        Returns:
            Response from Telegram API
        """
        if not emergency.get("is_emergency"):
            logger.info("send_emergency_alert called with is_emergency=False; skipping.")
            return {"success": False, "error": "Not an emergency"}
        
        severity_label = emergency.get("severity_label", "Manageable")
        severity_emoji = emergency.get("severity_emoji", "⚠️")
        symptom_summary = emergency.get("symptom_summary", "Symptoms reported")
        raw_message = emergency.get("raw_message", "")
        
        text = (
            "From: Carely (Emergency Alert)\n"
            f"User: {user_name}\n"
            f"💬 Reported Symptoms: {symptom_summary}\n"
            f"{severity_emoji} Severity: {severity_emoji} {severity_label}\n\n"
            "Please take appropriate action.\n"
            "Carely has started first-level comfort and monitoring responses for the user.\n\n"
            "---\n"
            f"User message: \"{raw_message}\""
        )
        
        chat_id = self.chat_id
        if not chat_id:
            logger.error("TELEGRAM_CHAT_ID not configured")
            return {"success": False, "error": "Chat ID not configured"}
        
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
        }
        
        try:
            url = f"{self.base_url}/sendMessage"
            response = requests.post(url, json=payload, timeout=10)
            result = response.json()
            
            if result.get("ok"):
                logger.info("Emergency alert sent successfully for user: %s", user_name)
                return {"success": True, "message_id": result.get("result", {}).get("message_id")}
            else:
                logger.error("Failed to send Telegram alert: %s", result.get("description"))
                return {"success": False, "error": result.get("description", "Unknown error")}
        except Exception as exc:
            logger.exception("Error sending Telegram alert: %s", exc)
            return {"success": False, "error": str(exc)}
    
    def _get_current_time(self) -> str:
        """Get current time in readable format"""
        from datetime import datetime
        return now_central().strftime("%I:%M %p, %B %d, %Y")

def send_emergency_alert(
    emergency: Dict[str, Any],
    user_name: str
) -> Dict[str, Any]:
    """
    Helper function to send emergency alert using severity from detection
    
    Args:
        emergency: Emergency detection result from CompanionAgent
        user_name: Name of the patient
        
    Returns:
        Response from Telegram API
    """
    notifier = TelegramNotifier()
    return notifier.send_emergency_alert(emergency, user_name)

def send_telegram_message(chat_id: str, message: str) -> Dict[str, Any]:
    """Helper function to send a simple Telegram message"""
    notifier = TelegramNotifier()
    return notifier.send_message(chat_id, message)
