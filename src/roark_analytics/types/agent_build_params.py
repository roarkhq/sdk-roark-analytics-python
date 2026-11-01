# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentBuildParams", "Llm", "Stt", "Tt"]


class Llm(TypedDict, total=False):
    """Optional text model the hosted agent thinks with. Roark's default when omitted"""

    model: Required[str]
    """The provider's model id, for example gpt-4.1"""

    provider: Required[Literal["OPENAI", "ANTHROPIC", "GOOGLE", "XAI", "ULTRAVOX", "AWS", "ELEVENLABS"]]
    """Text model provider, for example OPENAI"""


class Stt(TypedDict, total=False):
    """Optional transcriber the hosted agent hears with. Roark's default when omitted"""

    model: Required[str]
    """The provider's model id, for example nova-3"""

    provider: Required[Literal["DEEPGRAM", "OPENAI_WHISPER", "SPEECHMATICS", "ASSEMBLYAI", "ELEVENLABS"]]
    """Speech-to-text provider, for example DEEPGRAM"""


class Tt(TypedDict, total=False):
    """Optional provider voice the hosted agent speaks with"""

    provider: Required[Literal["CARTESIA", "ELEVENLABS", "OPENAI", "RIME"]]
    """Text-to-speech provider, for example ELEVENLABS"""

    voice_id: Required[Annotated[str, PropertyInfo(alias="voiceId")]]
    """The provider's id for the voice"""

    model: Optional[str]
    """
    The provider's voice model, for example eleven_flash_v2_5. Its current one when
    omitted
    """


class AgentBuildParams(TypedDict, total=False):
    job_description: Required[Annotated[str, PropertyInfo(alias="jobDescription")]]
    """
    One-line description of what the agent should do. Roark authors the system
    prompt from this.
    """

    name: Required[str]
    """Name of the agent"""

    llm: Optional[Llm]
    """Optional text model the hosted agent thinks with. Roark's default when omitted"""

    stt: Optional[Stt]
    """Optional transcriber the hosted agent hears with. Roark's default when omitted"""

    tts: Optional[Tt]
    """Optional provider voice the hosted agent speaks with"""

    voice: Optional[str]
    """
    Optional display name of the agent's voice. The authored prompt matches its
    delivery to it.
    """
