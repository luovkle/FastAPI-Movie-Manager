from fastapi import HTTPException, status


class Exceptions:
    TITLE_NOT_AVAILABLE = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Title not available",
    )
    NAME_NOT_AVAILABLE = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Name not available",
    )
    FILM_NOT_FOUND = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Film not found",
    )


exceptions = Exceptions()
