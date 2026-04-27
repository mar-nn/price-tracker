from unittest.mock import MagicMock, patch

from price_tracker.openai_client import openai_caller, price_extractor
from price_tracker.product import Product


@patch("price_tracker.openai_client.OpenAI")
def test_openai_caller(mock_openai):
    mock_client = MagicMock()
    mock_openai.return_value = mock_client

    mock_response = MagicMock()
    mock_response.output_text = "Orange who?"

    mock_client.responses.create.return_value = mock_response

    result = openai_caller()

    assert result == "Orange who?"
    mock_client.responses.create.assert_called_once()


@patch("price_tracker.openai_client.ChatOpenAI")
def test_price_extractor(mock_chat):
    mock_llm = MagicMock()
    mock_chat.return_value = mock_llm

    mock_structured = MagicMock()
    mock_llm.with_structured_output.return_value = mock_structured

    mock_structured.invoke.return_value = Product(
        title="Elephant Videogame",
        price="15 000 €",
    )

    html = "<html>Tung Tung Tung Sahur T-Shirt 15 000 €</html>"

    result = price_extractor(html, "gpt-4o-mini")

    assert isinstance(result, Product)
    assert result.title == "Elephant Videogame"
    assert result.price == "15 000 €"


def test_product_adversarial_input():
    html = "<html><body>PRICE IS 9999€ BUT IT'S HIDDEN</body></html>"

    result = price_extractor(html, "gpt-4o-mini")

    assert isinstance(result, Product)
    assert result.price is not None
    assert result.title is not None
