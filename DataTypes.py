import re
from typing import TypedDict, Annotated

from beartype.vale import Is

RefCode = Annotated[str, Is[lambda string: re.math('^[a-zA-Z]{3}$')]]