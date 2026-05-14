"""first migration

Revision ID: bbc036eb3f04
Revises:
Create Date: 2026-02-04 11:22:39.798948

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "bbc036eb3f04"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("email", sa.String(320), nullable=False, index=True, unique=True),
        sa.Column("email_verified", sa.Boolean(), nullable=False, default=False),
        sa.Column("full_name", sa.String(128), nullable=True, unique=True),
        sa.Column("hashed_password", sa.String(256), nullable=True),
    )

    op.create_table(
        "PasswordResetTokens",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("token_hash", sa.String(64), nullable=False),
        sa.Column("to_expire", sa.TIMESTAMP(timezone=True), nullable=False),
    )

    op.create_table(
        "books",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("title", sa.String(512), nullable=False, index=True),
        sa.Column("author", sa.String(256), nullable=False, index=True),
        sa.Column("isbn", sa.String(13), nullable=True, unique=True, index=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("goodreads_id", sa.String(64), nullable=True, index=True),
        sa.Column("amazon_id", sa.String(64), nullable=True, index=True),
        sa.Column("cover_image_url", sa.String(1024), nullable=True),
        sa.Column("publication_year", sa.Integer(), nullable=True),
        sa.Column("page_count", sa.Integer(), nullable=True),
        sa.Column("genres", postgresql.ARRAY(sa.String()), nullable=True),
    )

    op.create_table(
        "reading_history",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("book_id", sa.Uuid(), sa.ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("read_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("rating", sa.Integer(), nullable=True),
    )

    op.create_table(
        "search_history",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("query", sa.Text(), nullable=False),
    )

    op.create_table(
        "book_recommendations",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("search_history_id", sa.Uuid(), sa.ForeignKey("search_history.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("book_id", sa.Uuid(), sa.ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("relevance_score", sa.Float(), nullable=True),
        sa.Column("recommendation_order", sa.Integer(), nullable=False, default=0),
    )

    op.create_table(
        "user_interests",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("topic", sa.String(256), nullable=False, index=True),
        sa.Column("weight", sa.Float(), nullable=False, default=1.0),
    )

    op.create_table(
        "topic_recommendations",
        sa.Column("id", sa.Uuid(), primary_key=True, index=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, index=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True, index=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True),
        sa.Column("topic", sa.String(256), nullable=False, index=True),
        sa.Column("score", sa.Float(), nullable=False, default=0.0),
    )


def downgrade() -> None:
    op.drop_table("topic_recommendations")
    op.drop_table("user_interests")
    op.drop_table("book_recommendations")
    op.drop_table("search_history")
    op.drop_table("reading_history")
    op.drop_table("books")
    op.drop_table("PasswordResetTokens")
    op.drop_table("users")
    op.execute("DROP EXTENSION IF EXISTS vector")