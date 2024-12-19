import pytest
import pandas as pd


def test_get_unique_patients(mocker):
    mock_client = mocker.Mock()
    mock_query_result = mocker.Mock()

    # Mock the to_dataframe() method to return a DataFrame
    mock_query_result.to_dataframe.return_value = pd.DataFrame({"cnt_persons": [5]})

    mock_client.query.return_value = mock_query_result

    from app.database.querries import get_unique_patients
    result = get_unique_patients(mock_client, 7)

    assert result == 5
    mock_client.query.assert_called_once()

