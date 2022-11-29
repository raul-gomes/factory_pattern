from factory import TwitterAPIFactory, FacebookAPIFactory

def main() -> None:
    """Main function"""

    factories = {
        "twitter": TwitterAPIFactory(),
        "facebook": FacebookAPIFactory(),
    }
    queries = {
        "twitter": "elon musk",
        "facebook": "mark zuckerberg",
    }

    for factory in factories:
        api = factories[factory].create_api()
        api.connect(queries[factory])
    
if __name__ == "__main__":
    main()