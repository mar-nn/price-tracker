from unittest.mock import patch, MagicMock
from price_tracker.openai_client import (openai_caller, price_extractor)


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

    mock_response = MagicMock()
    mock_response.content = "15 000 €"

    mock_llm.invoke.return_value = mock_response

    html = "<html>Tung Tung Tung Sahur T-Shirt 15 000 €</html>"

    result = price_extractor(html, "gpt-4o-mini")

    assert "15 000 €" in result