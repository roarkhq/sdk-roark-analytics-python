# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallGetSentimentRunsResponse", "Data"]


class Data(BaseModel):
    status: str
    """Status of the sentiment run"""

    average_categorical_sentiment: Optional[str] = FieldInfo(alias="averageCategoricalSentiment", default=None)
    """NEUTRAL / NEGATIVE / POSITIVE"""

    average_sentiment: Optional[float] = FieldInfo(alias="averageSentiment", default=None)
    """Average sentiment score between 0-1 of the call"""

    common_emotion: Optional[str] = FieldInfo(alias="commonEmotion", default=None)
    """Common emotion of the call"""


class CallGetSentimentRunsResponse(BaseModel):
    data: Data
    """Sentiment run response payload"""
