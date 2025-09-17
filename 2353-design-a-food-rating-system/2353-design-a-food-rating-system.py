import heapq
from collections import defaultdict
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRating = {}    # food -> rating
        self.foodCuisine = {}   # food -> cuisine
        self.cuisineHeap = defaultdict(list)  # cuisine -> max heap of (-rating, food)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodRating[food] = rating
            self.foodCuisine[food] = cuisine
            heapq.heappush(self.cuisineHeap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.foodRating[food] = newRating
        cuisine = self.foodCuisine[food]
        # Push new entry into heap
        heapq.heappush(self.cuisineHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineHeap[cuisine]
        # Lazy deletion: pop until valid
        while heap:
            rating, food = heap[0]  # peek
            if -rating == self.foodRating[food]:
                return food
            heapq.heappop(heap)  # discard outdated entry
