#!/usr/bin/env python3
import requests
import json
import sys
from pprint import pprint

# Get the backend URL from the frontend .env file
import os
import re

def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            env_content = f.read()
            match = re.search(r'REACT_APP_BACKEND_URL=(.+)', env_content)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Error reading .env file: {e}")
    
    # Fallback
    return "https://632df3ed-719b-4efe-bc7b-8ed9ec1e4382.preview.emergentagent.com"

# Base URL for API requests
BASE_URL = get_backend_url()
API_URL = f"{BASE_URL}/api"

print(f"Testing backend API at: {BASE_URL}")

# Test results tracking
tests_passed = 0
tests_failed = 0
test_results = []

def run_test(test_name, test_func):
    global tests_passed, tests_failed
    print(f"\n===== Testing: {test_name} =====")
    try:
        result = test_func()
        if result:
            print(f"✅ PASS: {test_name}")
            tests_passed += 1
            test_results.append({"name": test_name, "status": "PASS"})
            return True
        else:
            print(f"❌ FAIL: {test_name}")
            tests_failed += 1
            test_results.append({"name": test_name, "status": "FAIL"})
            return False
    except Exception as e:
        print(f"❌ ERROR: {test_name} - {str(e)}")
        tests_failed += 1
        test_results.append({"name": test_name, "status": "ERROR", "message": str(e)})
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return False
    
    data = response.json()
    print("Response:")
    pprint(data)
    
    # Check required fields
    required_fields = ["message", "status", "version", "discord", "contact"]
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False
    
    # Check specific values
    if data["contact"] != "doddggy@mail.io":
        print(f"Incorrect contact email. Expected 'doddggy@mail.io', got '{data['contact']}'")
        return False
    
    if data["discord"] != "https://discord.gg/x2n3b6teqw":
        print(f"Incorrect Discord link. Expected 'https://discord.gg/x2n3b6teqw', got '{data['discord']}'")
        return False
    
    return True

def test_products_list():
    """Test the products list endpoint"""
    response = requests.get(f"{API_URL}/products")
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return False
    
    data = response.json()
    print("Response:")
    pprint(data)
    
    # Check if products key exists and is a list
    if "products" not in data or not isinstance(data["products"], list):
        print("Response doesn't contain a 'products' list")
        return False
    
    # Check if we have exactly 3 products
    if len(data["products"]) != 3:
        print(f"Expected 3 products, got {len(data['products'])}")
        return False
    
    # Check product data
    product_ids = [p["id"] for p in data["products"]]
    expected_ids = ["temp-spoofer", "perm-spoofer", "fortnite-cheat"]
    for expected_id in expected_ids:
        if expected_id not in product_ids:
            print(f"Missing product with ID: {expected_id}")
            return False
    
    # Check pricing for specific products
    for product in data["products"]:
        if product["id"] == "temp-spoofer":
            if product["weekly_price"] != 5.0 or product["monthly_price"] != 15.0:
                print(f"Incorrect pricing for temp-spoofer. Expected $5/$15, got ${product['weekly_price']}/${product['monthly_price']}")
                return False
        elif product["id"] == "perm-spoofer":
            if product["weekly_price"] != 15.0 or product["monthly_price"] != 40.0:
                print(f"Incorrect pricing for perm-spoofer. Expected $15/$40, got ${product['weekly_price']}/${product['monthly_price']}")
                return False
        elif product["id"] == "fortnite-cheat":
            if product["weekly_price"] != 10.0 or product["monthly_price"] != 30.0:
                print(f"Incorrect pricing for fortnite-cheat. Expected $10/$30, got ${product['weekly_price']}/${product['monthly_price']}")
                return False
    
    return True

def test_individual_product():
    """Test getting a specific product"""
    product_id = "temp-spoofer"
    response = requests.get(f"{API_URL}/products/{product_id}")
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return False
    
    data = response.json()
    print("Response:")
    pprint(data)
    
    # Check if product key exists
    if "product" not in data:
        print("Response doesn't contain a 'product' object")
        return False
    
    product = data["product"]
    
    # Check product ID
    if product["id"] != product_id:
        print(f"Expected product ID '{product_id}', got '{product['id']}'")
        return False
    
    # Check pricing
    if product["weekly_price"] != 5.0 or product["monthly_price"] != 15.0:
        print(f"Incorrect pricing. Expected $5/$15, got ${product['weekly_price']}/${product['monthly_price']}")
        return False
    
    return True

def test_contact_info():
    """Test the contact info endpoint"""
    response = requests.get(f"{API_URL}/contact")
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return False
    
    data = response.json()
    print("Response:")
    pprint(data)
    
    # Check required fields
    required_fields = ["email", "discord"]
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False
    
    # Check specific values
    if data["email"] != "doddggy@mail.io":
        print(f"Incorrect email. Expected 'doddggy@mail.io', got '{data['email']}'")
        return False
    
    if data["discord"] != "https://discord.gg/x2n3b6teqw":
        print(f"Incorrect Discord link. Expected 'https://discord.gg/x2n3b6teqw', got '{data['discord']}'")
        return False
    
    return True

def test_stats_endpoint():
    """Test the stats endpoint"""
    response = requests.get(f"{API_URL}/stats")
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return False
    
    data = response.json()
    print("Response:")
    pprint(data)
    
    # Check required fields
    required_fields = ["active_users", "uptime", "support", "products", "last_updated"]
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False
    
    # Check products count
    if data["products"] != 3:
        print(f"Expected 3 products, got {data['products']}")
        return False
    
    return True

def test_purchase_inquiry():
    """Test the purchase inquiry endpoint"""
    payload = {
        "product_name": "Temp Spoofer",
        "pricing_type": "weekly",
        "user_email": "test@example.com",
        "message": "I'm interested in purchasing this product."
    }
    
    response = requests.post(f"{API_URL}/contact/purchase", json=payload)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return False
    
    data = response.json()
    print("Response:")
    pprint(data)
    
    # Check required fields
    required_fields = ["message", "product", "pricing", "contact_methods", "instructions"]
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False
    
    # Check contact methods
    if "email" not in data["contact_methods"] or data["contact_methods"]["email"] != "doddggy@mail.io":
        print(f"Incorrect email in contact methods. Expected 'doddggy@mail.io', got '{data['contact_methods'].get('email')}'")
        return False
    
    if "discord" not in data["contact_methods"] or data["contact_methods"]["discord"] != "https://discord.gg/x2n3b6teqw":
        print(f"Incorrect Discord link in contact methods. Expected 'https://discord.gg/x2n3b6teqw', got '{data['contact_methods'].get('discord')}'")
        return False
    
    return True

def test_cors_headers():
    """Test that CORS headers are properly set"""
    response = requests.options(f"{API_URL}/products", headers={
        "Origin": "http://example.com",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "Content-Type"
    })
    
    print(f"Status Code: {response.status_code}")
    print("Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    
    # Check for CORS headers
    if "Access-Control-Allow-Origin" not in response.headers:
        print("Missing CORS header: Access-Control-Allow-Origin")
        return False
    
    if "Access-Control-Allow-Methods" not in response.headers:
        print("Missing CORS header: Access-Control-Allow-Methods")
        return False
    
    if "Access-Control-Allow-Headers" not in response.headers:
        print("Missing CORS header: Access-Control-Allow-Headers")
        return False
    
    return True

def run_all_tests():
    """Run all tests and print a summary"""
    print("\n========== FLUXWARE API TESTING ==========\n")
    
    # Run all tests
    run_test("Root Endpoint", test_root_endpoint)
    run_test("Products List", test_products_list)
    run_test("Individual Product", test_individual_product)
    run_test("Contact Info", test_contact_info)
    run_test("Stats Endpoint", test_stats_endpoint)
    run_test("Purchase Inquiry", test_purchase_inquiry)
    run_test("CORS Headers", test_cors_headers)
    
    # Print summary
    print("\n========== TEST SUMMARY ==========")
    print(f"Tests Passed: {tests_passed}")
    print(f"Tests Failed: {tests_failed}")
    print(f"Total Tests: {tests_passed + tests_failed}")
    
    # Print detailed results
    print("\nDetailed Results:")
    for result in test_results:
        status_symbol = "✅" if result["status"] == "PASS" else "❌"
        print(f"{status_symbol} {result['name']}: {result['status']}")
        if "message" in result:
            print(f"   Error: {result['message']}")
    
    # Return overall success/failure
    return tests_failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)