
from typing import Any

import aiohttp

__all__ = ["Request"]


class Request:
    @staticmethod
    async def get_json(
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """
        Sends a GET request and returns the response as JSON.

        Args:
            url (str): The URL to send the GET request to.
            params (Optional[Dict[str, Any]]): Query parameters to include in the request. Defaults to None.
            headers (Optional[Dict[str, str]]): Headers to include in the request. Defaults to None.

        Returns:
            Dict[str, Any]: The JSON response from the request.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as resp:
                return await resp.json()
