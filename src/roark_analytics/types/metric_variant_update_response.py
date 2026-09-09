# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricVariantUpdateResponse", "Data"]


class Data(BaseModel):
    """One named configuration of a metric."""

    id: str
    """Unique identifier for the variant."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the variant was created."""

    is_default: bool = FieldInfo(alias="isDefault")
    """Whether this is the variant a metric is scored with when nothing pins another."""

    is_system: bool = FieldInfo(alias="isSystem")
    """
    True for Roark's own variant, shared by every organization. Editing one forks it
    for yours; the original is left alone.
    """

    metric_definition_id: str = FieldInfo(alias="metricDefinitionId")
    """The metric this variant configures."""

    name: str
    """
    Name of the variant. "Default" is the one a metric is scored with unless
    something pins another.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the variant was last changed."""

    version_id: Optional[str] = FieldInfo(alias="versionId")
    """
    The variant's current version: an immutable snapshot of its configuration.
    Editing the variant advances this. Null only for a variant left without one,
    which cannot be scored until it is configured.
    """


class MetricVariantUpdateResponse(BaseModel):
    data: Data
    """One named configuration of a metric."""
