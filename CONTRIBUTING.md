# Contributing to InvoiceIQ

Thank you for your interest in contributing to InvoiceIQ! We welcome contributions from the community.

## 📋 How to Contribute

There are many ways to contribute to InvoiceIQ:

1. **Report bugs** - Use the [issue tracker](https://github.com/your-org/invoiceiq/issues)
2. **Suggest features** - Share your ideas for new features or improvements
3. **Improve documentation** - Help us make our docs clearer and more comprehensive
4. **Fix bugs** - Tackle open issues labeled as "bug"
5. **Add features** - Implement new functionality from our [roadmap](docs/ROADMAP.md)
6. **Review code** - Help review pull requests from other contributors

## 🛠️ Development Setup

### Prerequisites
- Node.js 18+
- Python 3.12+
- Git

### Getting Started

```bash
# Fork and clone the repository
git clone https://github.com/your-username/invoiceiq.git
cd invoiceiq

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies  
cd ../backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following our coding standards

3. Test your changes locally:
   ```bash
   # Backend tests
   cd backend
   python -m pytest
   
   # Frontend tests  
   cd ../frontend
   npm test
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

5. Push to your fork and open a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

## 💻 Coding Standards

### Backend (Python)
- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints extensively
- Write docstrings for all public functions and classes
- Keep functions focused and under 50 lines when possible
- Use descriptive variable and function names

### Frontend (TypeScript/React)
- Use TypeScript strict mode
- Follow React best practices and hooks rules
- Use functional components with hooks
- Keep components small and focused
- Use meaningful, descriptive names for variables and functions
- Follow the existing code style in the project

### Commit Messages
We follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding or modifying tests
- `chore:` for maintenance tasks

## 🧪 Testing

### Backend
```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=app

# Run specific test file
python -m pytest tests/test_specific_file.py
```

### Frontend
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test -- --coverage
```

### Type Checking
```bash
# Frontend
cd frontend
npm run type-check

# Backend (using mypy or pyright)
cd backend
mypy app/
```

## 📝 Documentation

- Update the README.md if your changes affect installation or usage
- Add docstrings/comments for new functions and classes
- Update API documentation if endpoints change
- Consider adding examples for complex functionality

## 🔍 Code Review Process

1. All pull requests require at least one approving review
2. CI checks must pass (tests, linting, type checking)
3. Keep PRs focused on a single change or feature
4. Write clear descriptions explaining what and why
5. Reference related issues in your PR description

## 🐛 Reporting Issues

When reporting bugs, please include:
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots or screen recordings if applicable
- Environment details (OS, browser version, etc.)
- Relevant logs or error messages

## 📄 License

By contributing to InvoiceIQ, you agree that your contributions will be licensed under the AGPL-3.0 license used by this project.

## ❓ Need Help?

If you have questions during the contribution process:
- Check existing issues to see if your question has been asked
- Join our community discussions
- Reach out to maintainers for guidance

Thank you for helping make InvoiceIQ better!