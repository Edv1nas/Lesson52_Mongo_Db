from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection


client = MongoClient("mongodb://localhost:27017/")
db = client["Warehouse"]
collection = db["Food"]


def filter_by_price_range(min_price: int, max_price: int) -> List[dict]:
    query = {"Price": {"$gte": min_price, "$lte": max_price}}
    result = collection.find(query)
    return list(result)


filtered_by_price_range = filter_by_price_range(5, 10)
# print(f"\n Food filtered by given price range: {filtered_by_price_range}")
for price in filtered_by_price_range:
    print(price["Name"], ":", price["Price"], "Eur")


def filter_food_by_name(collection: Collection, field_name: str, names: List[str]) -> List[dict]:
    query = {field_name: {"$in": names}}
    result = collection.find(query)
    return list(result)


names = ["onion", "gift", "stalk"]
filtered_food_by_name = filter_food_by_name(collection, "Name", names)
print(f"\n Food filtered by names: {filtered_food_by_name}")


def filter_food_by_excluded_names(collection: Collection, field_name: str, names: List[str]) -> List[dict]:
    query = {field_name: {"$nin": names}}
    result = collection.find(query)
    return list(result)


names = ["used", "macro", "ridge", "pool", "flock"]
filtered_food_by_excluded_names = filter_food_by_excluded_names(
    collection, "name", names)
print(f"\n Food filtered by excluded names: {filtered_food_by_excluded_names}")
