from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
from datetime import datetime

app = FastAPI(title="FluxWare API", description="Premium Gaming Tools API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Product(BaseModel):
    id: str
    name: str
    description: str
    weekly_price: float
    monthly_price: float
    features: List[str]

class ContactRequest(BaseModel):
    product_name: str
    pricing_type: str  # "weekly" or "monthly"
    user_email: Optional[str] = None
    message: Optional[str] = None

# In-memory product data (in a real app, this would be in a database)
PRODUCTS = [
    {
        "id": "temp-spoofer",
        "name": "Temp Spoofer",
        "description": "Resets on restart - Budget-friendly option for temporary identity masking",
        "weekly_price": 5.0,
        "monthly_price": 15.0,
        "features": ["Temporary protection", "Easy to use", "Budget-friendly", "Quick setup"]
    },
    {
        "id": "perm-spoofer",
        "name": "Perm Spoofer",
        "description": "Survives reboot and supports automatic updates for continuous protection",
        "weekly_price": 15.0,
        "monthly_price": 40.0,
        "features": ["Permanent protection", "Survives restarts", "Auto-updates", "Advanced features"]
    },
    {
        "id": "fortnite-cheat",
        "name": "Fortnite Public Cheat",
        "description": "Complete Fortnite enhancement suite with aimbot, ESP, anti-ban protection",
        "weekly_price": 10.0,
        "monthly_price": 30.0,
        "features": ["Aimbot system", "ESP/Wallhacks", "Anti-ban protection", "Regular updates"]
    }
]

@app.get("/")
async def root():
    return {
        "message": "FluxWare API is running",
        "status": "active",
        "version": "1.0.0",
        "discord": "https://discord.gg/x2n3b6teqw",
        "contact": "doddggy@mail.io"
    }

@app.get("/api/products")
async def get_products():
    """Get all available products"""
    return {"products": PRODUCTS}

@app.get("/api/products/{product_id}")
async def get_product(product_id: str):
    """Get a specific product by ID"""
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}

@app.post("/api/contact/purchase")
async def contact_for_purchase(request: ContactRequest):
    """Submit a purchase inquiry"""
    # Validate product exists
    product = next((p for p in PRODUCTS if p["name"].lower() in request.product_name.lower()), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # In a real application, you would:
    # 1. Store the inquiry in a database
    # 2. Send an email notification
    # 3. Log the interaction
    
    contact_info = {
        "email": "doddggy@mail.io",
        "discord": "https://discord.gg/x2n3b6teqw",
        "discord_server": "FluxWare Official"
    }
    
    return {
        "message": "Purchase inquiry received",
        "product": request.product_name,
        "pricing": request.pricing_type,
        "contact_methods": contact_info,
        "instructions": "Please contact us via email or Discord to complete your purchase. Include the product name and pricing option in your message."
    }

@app.get("/api/contact")
async def get_contact_info():
    """Get contact information"""
    return {
        "email": "doddggy@mail.io",
        "discord": "https://discord.gg/x2n3b6teqw",
        "discord_server": "FluxWare Official",
        "support_hours": "24/7 Discord Support"
    }

@app.get("/api/stats")
async def get_stats():
    """Get site statistics"""
    return {
        "active_users": "1000+",
        "uptime": "99.9%",
        "support": "24/7",
        "products": len(PRODUCTS),
        "last_updated": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)