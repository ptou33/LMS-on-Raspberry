#!/bin/bash

# Resolve the absolute path of the script (no matter where it's called from)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to the virtual environment
VENV_DIR="$SCRIPT_DIR/env"

# Create the venv if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the venv
source "$VENV_DIR/bin/activate"

# Install yt-dlp if not already installed
if ! python -c "import yt_dlp" &>/dev/null; then
    echo "Installing yt-dlp..."
    pip install --upgrade pip yt-dlp
fi

# Run the downloader script
python "$SCRIPT_DIR/youtube_full_quality_downloader.py" "$@"

# Deactivate venv
deactivate
