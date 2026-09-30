# Real Estate AI Assistant

An AI-powered assistant for exploring real estate listings and answering property-related questions.

## Features

- Search properties by location, budget, and preferences
- Ask natural-language questions about listings
- Compare properties by price, size, and amenities
- Summarize listing details for buyers and renters

## Getting Started

### Prerequisites

- Python 3.10 or later
- An API key for the AI provider used by the application

### Installation

```bash
git clone <repository-url>
cd real_estate_ai_assistant
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add the required credentials:

```env
AI_API_KEY=your_api_key_here
```

Never commit API keys or other secrets to version control.

## Running the Application

```bash
python app.py
```

Replace `app.py` with the project’s actual entry point if it differs.

## Example Questions

- “Find two-bedroom homes within my budget.”
- “Compare these properties by price and location.”
- “What should I consider before making an offer?”

Always verify listing information with the listing provider or a qualified real estate professional.

## Development

Run the project’s tests and formatting checks before submitting changes.

## License

Add the project license information here.
