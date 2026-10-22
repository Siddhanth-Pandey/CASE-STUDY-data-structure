"""
City Navigation + Huffman Compression Case Study
------------------------------------------------
A self-contained Python demonstration of:
1. A city road network represented as a weighted, undirected graph.
2. Dijkstra's algorithm for shortest routes.
3. Breadth-first search (BFS) for reachability.
4. Huffman coding for frequency-based text compression.
5. GZIP and ZIP archive creation using Python's standard library.

Run:
    python city_navigation_compression.py

No third-party packages are required.
"""

from __future__ import annotations

import gzip
import heapq
import json
import zipfile
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ----------------------------- City graph ---------------------------------

@dataclass
class HuffmanNode:
    frequency: int
    character: Optional[str] = None
    left: Optional["HuffmanNode"] = None
    right: Optional["HuffmanNode"] = None

    def __lt__(self, other: "HuffmanNode") -> bool:
        # Tie-break deterministically by frequency, then character/tree marker.
        return (self.frequency, self.character or "") < (
            other.frequency, other.character or ""
        )


class CityMap:
    """Weighted undirected graph: intersections are nodes, roads are edges."""

    def __init__(self) -> None:
        self.graph: Dict[str, Dict[str, float]] = {}

    def add_road(self, start: str, end: str, distance_km: float) -> None:
        if distance_km <= 0:
            raise ValueError("Road distance must be positive.")
        self.graph.setdefault(start, {})
        self.graph.setdefault(end, {})
        self.graph[start][end] = distance_km
        self.graph[end][start] = distance_km

    def shortest_path(self, source: str, destination: str) -> Tuple[List[str], float]:
        """Return shortest path and distance using Dijkstra's algorithm."""
        if source not in self.graph or destination not in self.graph:
            raise ValueError("Source and destination must exist in the city map.")

        distances = {node: float("inf") for node in self.graph}
        previous: Dict[str, Optional[str]] = {node: None for node in self.graph}
        distances[source] = 0.0
        queue = [(0.0, source)]

        while queue:
            distance, node = heapq.heappop(queue)
            if distance != distances[node]:
                continue
            if node == destination:
                break

            for neighbor, weight in self.graph[node].items():
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    previous[neighbor] = node
                    heapq.heappush(queue, (candidate, neighbor))

        if distances[destination] == float("inf"):
            return [], float("inf")

        path = []
        current: Optional[str] = destination
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path, distances[destination]

    def reachable_from(self, source: str) -> List[str]:
        """Return all nodes reachable from source using BFS."""
        if source not in self.graph:
            raise ValueError(f"Unknown location: {source}")
        visited = {source}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return sorted(visited)


# ---------------------------- Huffman coding ------------------------------

def build_huffman_tree(text: str) -> Optional[HuffmanNode]:
    if not text:
        return None

    frequencies = Counter(text)
    heap = [HuffmanNode(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Special case: a one-symbol alphabet still needs a non-empty code.
    if len(heap) == 1:
        only = heapq.heappop(heap)
        return HuffmanNode(only.frequency, None, only, None)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(left.frequency + right.frequency, None, left, right)
        heapq.heappush(heap, parent)
    return heap[0]


def build_code_table(root: Optional[HuffmanNode]) -> Dict[str, str]:
    codes: Dict[str, str] = {}
    if root is None:
        return codes

    def visit(node: HuffmanNode, prefix: str) -> None:
        if node.character is not None:
            codes[node.character] = prefix or "0"
            return
        if node.left is not None:
            visit(node.left, prefix + "0")
        if node.right is not None:
            visit(node.right, prefix + "1")

    visit(root, "")
    return codes


def huffman_encode(text: str, codes: Dict[str, str]) -> str:
    return "".join(codes[character] for character in text)


def huffman_decode(bits: str, root: Optional[HuffmanNode]) -> str:
    if root is None:
        return ""
    # Handle the one-character alphabet.
    if root.left is not None and root.right is None and root.left.character is not None:
        if any(bit != "0" for bit in bits):
            raise ValueError("Invalid bit stream for one-character Huffman tree.")
        return root.left.character * len(bits)

    decoded: List[str] = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right if bit == "1" else None
        if node is None:
            raise ValueError("Invalid Huffman bit stream.")
        if node.character is not None:
            decoded.append(node.character)
            node = root
    if node is not root:
        raise ValueError("Incomplete Huffman code at end of bit stream.")
    return "".join(decoded)


def huffman_demo(text: str) -> dict:
    root = build_huffman_tree(text)
    codes = build_code_table(root)
    encoded = huffman_encode(text, codes)
    decoded = huffman_decode(encoded, root)
    return {
        "original_text": text,
        "frequencies": dict(sorted(Counter(text).items())),
        "codes": dict(sorted(codes.items())),
        "encoded_bits": encoded,
        "encoded_bit_length": len(encoded),
        "original_8bit_length": len(text.encode("utf-8")) * 8,
        "decoded_matches_original": decoded == text,
    }


# ---------------------------- Sample scenario -----------------------------

def build_sample_city() -> CityMap:
    city = CityMap()
    roads = [
        ("Central Station", "City Hall", 2.0),
        ("Central Station", "Museum", 4.0),
        ("City Hall", "Market Square", 1.5),
        ("City Hall", "University", 3.0),
        ("Market Square", "Riverside Park", 2.5),
        ("Museum", "University", 1.0),
        ("University", "Tech Park", 2.0),
        ("Riverside Park", "Tech Park", 4.0),
        ("Market Square", "Tech Park", 5.0),
    ]
    for start, end, distance in roads:
        city.add_road(start, end, distance)
    return city


def write_compression_files(report_text: str, output_dir: Path) -> dict:
    """Write report.txt, report.txt.gz and report_bundle.zip."""
    text_path = output_dir / "sample_report.txt"
    gzip_path = output_dir / "sample_report.txt.gz"
    zip_path = output_dir / "sample_report_bundle.zip"

    text_path.write_text(report_text, encoding="utf-8")
    with gzip.open(gzip_path, "wt", encoding="utf-8") as compressed:
        compressed.write(report_text)

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(text_path, arcname="sample_report.txt")

    return {
        "text_file": text_path.name,
        "gzip_file": gzip_path.name,
        "zip_file": zip_path.name,
        "text_bytes": text_path.stat().st_size,
        "gzip_bytes": gzip_path.stat().st_size,
        "zip_bytes": zip_path.stat().st_size,
    }


def main() -> None:
    output_dir = Path(__file__).resolve().parent
    city = build_sample_city()

    source = "Central Station"
    destination = "Tech Park"
    path, distance = city.shortest_path(source, destination)
    reachable = city.reachable_from(source)

    report_lines = [
        "CITY NAVIGATION CASE STUDY",
        f"Route: {source} -> {destination}",
        f"Shortest path: {' -> '.join(path)}",
        f"Total distance: {distance:.1f} km",
        f"Reachable locations from {source}: {', '.join(reachable)}",
        "",
        "Algorithm: Dijkstra's shortest-path algorithm",
        "Graph model: weighted, undirected graph",
    ]
    report_text = "\n".join(report_lines) + "\n"
    huffman = huffman_demo(report_text)
    file_info = write_compression_files(report_text, output_dir)

    print("=== CITY NAVIGATION ===")
    print(f"Start: {source}")
    print(f"Destination: {destination}")
    print("Shortest route:", " -> ".join(path))
    print(f"Total distance: {distance:.1f} km")
    print("Reachable locations:", ", ".join(reachable))
    print()
    print("=== HUFFMAN CODING ===")
    print(f"Unique characters: {len(huffman['frequencies'])}")
    print(f"Encoded bit length: {huffman['encoded_bit_length']}")
    print(f"Original 8-bit length: {huffman['original_8bit_length']}")
    print("Decode verification:", "PASS" if huffman["decoded_matches_original"] else "FAIL")
    print()
    print("=== FILE COMPRESSION ===")
    print(f"Plain text: {file_info['text_file']} ({file_info['text_bytes']} bytes)")
    print(f"GZIP:      {file_info['gzip_file']} ({file_info['gzip_bytes']} bytes)")
    print(f"ZIP:       {file_info['zip_file']} ({file_info['zip_bytes']} bytes)")
    print("Note: tiny files can become larger after compression due to archive headers.")

    (output_dir / "huffman_report.json").write_text(
        json.dumps(huffman, indent=2, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
