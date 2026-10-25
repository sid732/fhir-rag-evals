"""List prices for cost reporting. Cost is always derived from recorded usage.

USD per million tokens, from Anthropic's model table dated 2026-10-06. Cache
writes bill at 1.25x input and cache reads at 0.1x. Update this table when
prices change; reports name the model, so old reports stay interpretable.
"""

from fhir_rag.llm.client import Usage

PRICES: dict[str, tuple[float, float]] = {
    "claude-opus-5-5": (4.00, 20.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-fable-5-1": (10.00, 50.00),
    "claude-opus-4-8": (5.00, 25.00),  # a possible refusal fallback
}


def cost_usd(model: str, usage: Usage) -> float | None:
    """Dollar cost of one call, or None when the model has no listed price."""
    price = PRICES.get(model)
    if price is None:
        return None
    per_in, per_out = (p / 1_000_000 for p in price)
    return (
        usage.input_tokens * per_in
        + usage.output_tokens * per_out
        + usage.cache_read_input_tokens * per_in * 0.1
        + usage.cache_creation_input_tokens * per_in * 1.25
    )
