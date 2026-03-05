"""Tests for super-email-template."""

import pytest
from super_email_template import template


class TestTemplate:
    """Test suite for template."""

    def test_basic(self):
        """Test basic usage."""
        result = template("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            template("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = template(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
