"""
Unit tests for logging utilities module.
"""

import pytest
import logging
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.logging_utils import setup_logging, logger, handle_api_error, safe_execute


class TestLoggingUtils:
    """Test cases for logging utilities"""

    def test_setup_logging(self):
        """Test logging setup"""
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = str(Path(temp_dir) / "test.log")
            test_logger = setup_logging(log_file=log_file)

            # Check that logger is configured
            assert test_logger.level <= logging.INFO
            assert len(test_logger.handlers) > 0

            # Clean up handlers to avoid file locking
            for handler in test_logger.handlers:
                handler.close()
            test_logger.handlers.clear()

    def test_logger_instance(self):
        """Test that logger is properly instantiated"""
        assert isinstance(logger, logging.Logger)
        assert logger.name == "gitsensei"

    @patch("src.logging_utils.logger")
    def test_handle_api_error(self, mock_logger):
        """Test API error handling"""
        test_error = Exception("Test API error")

        # Test with fallback
        result = handle_api_error(test_error, "test operation", fallback="fallback")
        assert result == "fallback"
        mock_logger.error.assert_called_once()

    def test_safe_execute_success(self):
        """Test safe_execute with successful function"""

        def test_func():
            return "success"

        result = safe_execute(test_func)
        assert result == "success"

    def test_safe_execute_failure(self):
        """Test safe_execute with failing function"""

        def failing_func():
            raise ValueError("Test error")

        result = safe_execute(failing_func, fallback="default")
        assert result == "default"

    @patch("src.logging_utils.logger")
    def test_safe_execute_logging(self, mock_logger):
        """Test that safe_execute logs errors"""

        def failing_func():
            raise RuntimeError("Test runtime error")

        result = safe_execute(failing_func, fallback=None)
        assert result is None
        mock_logger.error.assert_called_once()
