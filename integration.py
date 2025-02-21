integration_json={
  "data": {
    "date": {
      "created_at": "2025-02-19",
      "updated_at": "2025-02-19"
    },
    "descriptions": {
      "app_description": "Fetches local events based on chosen city or location and posts updates on the Telex channel",
      "app_logo": "https://my-portfolio-343207.web.app/MyLogo2.png",
      "app_name": "Local event Notifier.",
      "app_url": "URL to the application or service.", 
      "background_color": "#ffffff",
    },
    "integration_category": "Social Media Management",
    "integration_type": "interval",
    "is_active": True,
    "output": [
      {
        "label": "output_channel_1",
        "value": True
      },
      {
        "label": "output_channel_2",
        "value": False
      }
    ],
    "key_features": [
      "Fetches events based on city, and category.",
      "Sends events to Telex.",
      "Notifys users of events.",
      "post events at intervals."
    ],
    "permissions": {
      "monitoring_user": {
        "always_online": True,
        "display_name": "Performance Monitor"
      }
    },
    "settings": [
      {
        "label": "interval",
        "type": "text",
        "required": True,
        "default": "* * * * *"
      },
      {
        "label": "location",
        "type": "text",
        "required": True,
        "default": "Berlin"
      },
      {
        "label": "limit",
        "type": "text",
        "required": True,
        "default": "10"
      },
  
      {
        "label": "category",
        "type": "dropdown",
        "required": True,
        "default": "Music",
        "options": ["Music", "Arts", "Sports", "Food", "Business", "Tech", "Health", "Science", "Education", "Fashion", "Film", "Literature", "Religion", "Politics", "Charity", "Community", "Family", "Holiday", "Other"]
      }
 
    ],
    "tick_url": "https://local-event-notifier.vercel.app/api/tick",
    "target_url": "https://ping.telex.im/v1/webhooks/01951fa7-6d0e-753d-ba67-e9ea376bcce4"
  }
}