"""Sistema de recomendación simple basado en coincidencia de palabras clave.

Actividad formativa: GitHub Copilot.
El programa usa únicamente la biblioteca estándar de Python.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Iterable

DATA_FILE = Path(__file__).with_name("products.csv")


def normalize(text: str) -> list[str]:
    """Convierte un texto en una lista de palabras normalizadas."""
    return re.findall(r"[a-záéíóúñ0-9]+", text.lower())


def load_products(path: Path = DATA_FILE) -> list[dict[str, str]]:
    """Carga los productos desde un archivo CSV."""
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def product_terms(product: dict[str, str]) -> set[str]:
    """Obtiene las palabras relevantes de un producto."""
    text = " ".join(
        [
            product.get("name", ""),
            product.get("category", ""),
            product.get("tags", ""),
        ]
    )
    return set(normalize(text))


def score_product(
    product: dict[str, str], interests: Iterable[str]
) -> tuple[int, list[str]]:
    """Calcula puntaje y coincidencias entre un producto y los intereses."""
    terms = product_terms(product)
    matches = sorted({interest for interest in interests if interest in terms})

    # Cada palabra coincidente aporta un punto.
    score = len(matches)

    # Se otorga un punto extra si el interés coincide con la categoría.
    category_terms = set(normalize(product.get("category", "")))
    if any(interest in category_terms for interest in matches):
        score += 1

    return score, matches


def explain_recommendation(product: dict[str, str], matches: Iterable[str]) -> str:
    """Explica qué intereses coincidieron y en qué campos del producto."""
    fields = {
        "nombre": set(normalize(product.get("name", ""))),
        "categoría": set(normalize(product.get("category", ""))),
        "etiquetas": set(normalize(product.get("tags", ""))),
    }
    details = []

    for interest in matches:
        locations = [name for name, terms in fields.items() if interest in terms]
        details.append(f"{interest} ({', '.join(locations)})")

    return f"Recomendado porque coincide con tus intereses en: {', '.join(details)}."


def recommend(
    products: list[dict[str, str]],
    user_interests: str,
    top_n: int = 3,
) -> list[dict[str, object]]:
    """Retorna las mejores recomendaciones para los intereses indicados."""
    interests = list(dict.fromkeys(normalize(user_interests)))
    results: list[dict[str, object]] = []

    for product in products:
        score, matches = score_product(product, interests)
        if score > 0:
            results.append(
                {
                    "product": product,
                    "score": score,
                    "matches": matches,
                    "explanation": explain_recommendation(product, matches),
                }
            )

    results.sort(
        key=lambda item: (
            int(item["score"]),
            str(item["product"]["name"]),
        ),
        reverse=True,
    )

    return results[:top_n]


def ask_top_n() -> int:
    """Solicita al usuario la cantidad de recomendaciones."""
    raw = input("¿Cuántas recomendaciones deseas ver? [3]: ").strip()
    if not raw:
        return 3

    try:
        value = int(raw)
        return max(1, min(value, 10))
    except ValueError:
        print("Valor no válido. Se mostrarán 3 recomendaciones.")
        return 3


def main() -> None:
    """Ejecuta la interfaz básica del recomendador."""
    print("=== Sistema de recomendación con IA: ejemplo académico ===")
    interests = input("Ingresa tus intereses separados por comas: ").strip()

    if not interests:
        print("Debes ingresar al menos un interés.")
        return

    top_n = ask_top_n()

    try:
        products = load_products()
    except FileNotFoundError as error:
        print(error)
        return

    recommendations = recommend(products, interests, top_n)

    if not recommendations:
        print("\nNo se encontraron coincidencias. Prueba con otros intereses.")
        return

    print("\nRecomendaciones:")
    for index, item in enumerate(recommendations, start=1):
        product = item["product"]
        matches = item["matches"]

        print(
            f"{index}. {product['name']} - Puntaje: {item['score']}\n"
            f"   Categoría: {product['category']}\n"
            f"   Coincidencias: {', '.join(matches)}\n"
            f"   Motivo: {item['explanation']}\n"
            f"   Precio referencial: {product['price']}\n"
        )


if __name__ == "__main__":
    main()
