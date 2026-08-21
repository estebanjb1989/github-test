import os


def charge_live_stripe_customer():
    if os.environ.get("NEXT_PUBLIC_ENVIRONMENT") != "prod":
        print("Skipping live Stripe charge — not running in prod.")
        return
    print("Charging real customer via live Stripe keys")
