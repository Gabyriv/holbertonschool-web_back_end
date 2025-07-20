# Caching

A Python implementation of various caching algorithms that inherit from a base caching class. This project demonstrates different cache replacement policies including Basic Cache, FIFO (First In, First Out), LIFO (Last In, First Out), and LRU (Least Recently Used).

## Project Structure

```
caching/
├── base_caching.py      # Base caching class with common functionality
├── 0-basic_cache.py     # Basic cache implementation
├── 0-main.py           # Test file for basic cache
├── 1-fifo_cache.py     # FIFO cache implementation
├── 1-main.py           # Test file for FIFO cache
├── 2-lifo_cache.py     # LIFO cache implementation
├── 3-lru_cache.py      # LRU cache implementation
├── 4-mru_cache.py      # MRU cache implementation
└── README.md           # This file
```

## Cache Implementations

### BaseCaching
The parent class that provides the foundation for all cache implementations:
- `MAX_ITEMS`: Maximum number of items allowed in the cache
- `cache_data`: Dictionary to store cache items
- Abstract `put()` and `get()` methods

### BasicCache
A simple cache implementation that stores items without any replacement policy:
- Stores items up to `MAX_ITEMS`
- No automatic eviction when cache is full
- Inherits all functionality from `BaseCaching`

### FIFOCache (First In, First Out)
Implements FIFO replacement policy:
- When cache is full, removes the **oldest** item (first one added)
- Uses `next(iter(self.cache_data))` to get the first key
- Prints `DISCARD: {key}` when removing items

### LIFOCache (Last In, First Out)
Implements LIFO replacement policy:
- When cache is full, removes the **newest** item (last one added)
- Uses `list(self.cache_data.keys())[-1]` to get the last key
- Prints `DISCARD: {key}` when removing items

### LRUCache (Least Recently Used)
Implements LRU replacement policy:
- When cache is full, removes the **least recently accessed** item
- Tracks access order using `self.access_order` list
- Updates access order on both `put()` and `get()` operations
- Prints `DISCARD: {key}` when removing items

### MRUCache (Most Recently Used)
Implements MRU replacement policy:
- When cache is full, removes the **most recently accessed** item
- Tracks access order using `self.access_order` list
- Updates access order on both `put()` and `get()` operations
- Prints `DISCARD: {key}` when removing items

## Usage Examples

### Basic Cache
```python
from 0-basic_cache import BasicCache

cache = BasicCache()
cache.put("A", 1)
cache.put("B", 2)
print(cache.get("A"))  # Output: 1
```

### FIFO Cache
```python
from 1-fifo_cache import FIFOCache

cache = FIFOCache()
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)  # If cache is full, removes "A" (first item)
print(cache.get("A"))  # Output: None (was removed)
```

### LIFO Cache
```python
from 2-lifo_cache import LIFOCache

cache = LIFOCache()
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)  # If cache is full, removes "B" (last item added)
print(cache.get("B"))  # Output: None (was removed)
```

### LRU Cache
```python
from 3-lru_cache import LRUCache

cache = LRUCache()
cache.put("A", 1)
cache.put("B", 2)
cache.get("A")     # Makes "A" most recently used
cache.put("C", 3)  # If cache is full, removes "B" (least recently used)
print(cache.get("B"))  # Output: None (was removed)
```

### MRU Cache
```python
from 4-mru_cache import MRUCache

cache = MRUCache()
cache.put("A", 1)
cache.put("B", 2)
cache.get("A")     # Makes "A" most recently used
cache.put("C", 3)  # If cache is full, removes "A" (most recently used)
print(cache.get("A"))  # Output: None (was removed)
```

## Testing

Each cache implementation includes a corresponding test file:
- `0-main.py` - Tests BasicCache
- `1-main.py` - Tests FIFOCache
- Additional test files can be created for LIFO and LRU caches

Run tests with:
```bash
python3 0-main.py
python3 1-main.py
```

## Key Features

- **Inheritance-based design**: All caches inherit from `BaseCaching`
- **Consistent interface**: All caches implement the same `put()` and `get()` methods
- **Proper error handling**: Handles None keys and items gracefully
- **Clear output**: Prints discarded items with descriptive messages
- **Memory efficient**: Automatically manages cache size limits

## Algorithm Comparison

| Cache Type | Replacement Policy | When Full, Removes |
|------------|-------------------|-------------------|
| Basic      | None              | No automatic removal |
| FIFO       | First In, First Out | Oldest item added |
| LIFO       | Last In, First Out | Newest item added |
| LRU        | Least Recently Used | Least recently accessed |
| MRU        | Most Recently Used | Most recently accessed |

## Requirements

- Python 3.7+ (for dictionary insertion order preservation)
- No external dependencies required

## Author

This project is part of the Holberton School curriculum, demonstrating advanced Python concepts including inheritance, data structures, and algorithm implementation.
