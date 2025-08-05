from datetime import datetime, timezone
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__: str = "users"

    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    created_at: str = Field(default=lambda: datetime.now(timezone.utc), nullable=False)


class Vault(SQLModel, table=True):
    __tablename__: str = "vaults"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    user_id: int = Field(foreign_key="users.id", nullable=False)


class PasswordEntry(SQLModel, table=True):
    __tablename__: str = "password_entries"

    id: int = Field(default=None, primary_key=True)
    vault_id: int = Field(foreign_key="vaults.id", nullable=False)
    title: str = Field(nullable=False)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    url: str = Field(default=None, nullable=True)
    notes: str = Field(default=None, nullable=True)
    created_at: str = Field(default=lambda: datetime.now(timezone.utc), nullable=False)


class Tag(SQLModel, table=True):
    __tablename__: str = "tags"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False)


class EntryTagLink(SQLModel, table=True):
    __tablename__: str = "entry_tag_links"
    
    entry_id: int = Field(foreign_key="password_entries.id", primary_key=True)
    tag_id: int = Field(foreign_key="tags.id", primary_key=True)
