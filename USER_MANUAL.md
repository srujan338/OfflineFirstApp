# InvoiceIQ User Manual

## Introduction

InvoiceIQ is a privacy-focused, offline-first application that converts your invoices and receipts into structured financial data. All processing happens locally on your CPU - no data leaves your device, no internet connection is required after initial setup, and no GPU is needed.

This guide will walk you through using InvoiceIQ to manage your expenses, understand your spending patterns, and maintain complete control over your financial data.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Processing Your First Invoice](#processing-your-first-invoice)
3. [Managing Your Invoices](#managing-your-invoices)
4. [Understanding Your Spending](#understanding-your-spending)
5. [Advanced Features](#advanced-features)
6. [Troubleshooting](#troubleshooting)
7. [Privacy & Security](#privacy--security)

---

## Getting Started

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+, Fedora 35+)
- **Processor**: Modern CPU (Intel i3/Ryzen 3 or better recommended)
- **Memory**: 4GB RAM minimum, 8GB+ recommended
- **Storage**: 500MB available space (database grows with your data)
- **Browser**: Modern Chrome, Firefox, Safari, or Edge (for the web interface)

### Installation

#### Option 1: Desktop Application (Recommended)
1. Download the installer for your OS from [github.com/your-org/invoiceiq/releases](https://github.com/your-org/invoiceiq/releases)
2. Run the installer and follow the prompts
3. Launch InvoiceIQ from your applications menu

#### Option 2: Web Application
1. Ensure you have Node.js 18+ installed
2. Clone the repository: `git clone https://github.com/your-org/invoiceiq.git`
3. Navigate to the project: `cd invoiceiq`
4. Install dependencies: 
   ```bash
   cd frontend && npm install
   cd ../backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
   ```
5. Start the backend: `uvicorn app.main:app --reload`
6. Start the frontend: `cd ../frontend && npm run dev`
7. Open http://localhost:3000 in your browser

### First Launch
When you first open InvoiceIQ:
1. The application will set up a local SQLite database to store your invoice data
2. You'll be taken to the main dashboard
3. No account creation or email verification is required

## Processing Your First Invoice

### Supported File Formats
InvoiceIQ accepts:
- **Images**: JPG, JPEG, PNG, BMP, TIFF
- **Documents**: PDF (single or multi-page)

### Methods of Input

#### 1. File Upload
1. Click the "Upload Invoice" button on the dashboard
2. Select one or more invoice files from your computer
3. Wait for processing to complete (usually 1-5 seconds per page)
4. Review the extracted data in the verification form
5. Make any necessary corrections
6. Click "Save Invoice" to store the data

#### 2. Drag & Drop
1. Drag invoice files from your file explorer
2. Drop them onto the designated upload area
3. Follow steps 3-6 from above

#### 3. Camera/Mobile (PWA Feature)
If installed as a Progressive Web App:
1. Tap the camera icon
2. Grant camera permission when prompted
3. Position the invoice in the frame
4. Capture the image
5. Review and save as described above

### What InvoiceIQ Extracts
The AI engine attempts to extract:
- **Vendor/Supplier Name** - Who issued the invoice
- **Invoice Number** - Unique identifier
- **Date** - Invoice date
- **Line Items** - Individual products/services with prices
- **Subtotal** - Before tax amount
- **Tax** - Sales tax/VAT amount
- **Total** - Final amount due
- **Currency** - Detected from symbols or context
- **Payment Terms** - When payment is due (if specified)

### Verification & Correction
After processing, you'll see a form with the extracted data:
1. Review each field for accuracy
2. Click on any field to edit it directly
3. Use the "Add Line Item" button if items were missed
4. Use the trash can icon to remove incorrect line items
5. Select the correct category from the dropdown
6. Add notes if needed (for personal reference)
7. Click "Save Invoice" to store the corrected data

## Managing Your Invoices

### Dashboard Overview
The main dashboard shows:
- **Summary Cards**: Total spent, transaction count, average transaction
- **Recent Activity**: Latest invoices processed
- **Spending Chart**: Visual representation of expenses by category
- **Quick Actions**: Upload new invoice, filter options

### Browsing & Searching
- **Date Navigation**: Use the calendar to jump to specific months
- **Category Filter**: Click category buttons to show/hide expenses
- **Search Bar**: Type vendor names, amounts, or notes to filter results
- **Sort Options**: Click column headers to sort by date, amount, or vendor

### Individual Invoice Details
Click any invoice in the list to view:
- Complete extracted data
- Original image/preview (if available)
- Processing metrics (OCR time, parsing time)
- Edit history (if you've made corrections)
- Option to re-process with different settings

### Editing Existing Invoices
1. Open an invoice from the list
2. Click the "Edit" button
3. Make changes to any field
4. Adjust line items as needed
5. Update category if desired
6. Click "Save Changes"

### Deleting Invoices
1. Select one or more invoices using checkboxes
2. Click the "Delete" button that appears
3. Confirm the deletion in the popup dialog
4. Note: This action cannot be undone

## Understanding Your Spending

### Analytics Dashboard
Access the analytics section via the sidebar navigation to see:

#### Spending by Category
- Pie chart showing percentage distribution
- Bar chart comparing month-over-month spending
- Top spending categories listed numerically

#### Trends Over Time
- Line chart showing daily/weekly/monthly spending
- Moving averages to identify spending patterns
- Comparison to previous periods

#### Vendor Analysis
- Most frequent vendors
- Average spend per vendor
- Spending trends with specific merchants

#### Income vs Expenses (if applicable)
- Net cash flow visualization
- Savings rate calculation
- Budget vs actual tracking

### Custom Reports
1. Click "Generate Report" in the analytics section
2. Select date range (custom, last 7 days, last 30 days, etc.)
3. Choose categories to include/exclude
4. Select output format (PDF, CSV, Excel)
5. Click "Generate" to download your report

### Exporting Data
- **CSV Export**: All invoice data in spreadsheet format
- **JSON Export**: Complete data structure for developers
- **PDF Summary**: Printable report with charts and summaries
- **Backup**: Complete database export for migration or backup purposes

## Advanced Features

### Category Management
InvoiceIQ learns from your corrections:
1. When you change a category, the system notes the vendor and your choice
2. Future invoices from the same vendor will default to your selected category
3. To manage learned categories:
   - Go to Settings → Categories
   - View, rename, or delete learned associations
   - Reset all learning data if needed

### Processing Settings
Adjust OCR and parsing behavior:
- **Language**: Select OCR language(s) for multi-language invoices
- **Confidence Threshold**: Adjust how certain the AI must be to auto-accept
- **Preprocessing**: Toggle image enhancement options
- **PDF Handling**: Choose single-page vs multi-page processing modes

### Automation & Integration
- **Watch Folders**: Configure folders to auto-process when files are added
- **Command Line Interface**: Process batches of invoices via terminal
- **API Access**: Use the RESTful API for custom integrations
- **Webhooks**: Send processed data to other applications (when online)

### Multi-Device Usage
While primarily designed for single-device use:
1. **Backup & Restore**: Export from one device, import to another
2. **Scheduled Backups**: Automatic exports to cloud storage (optional)
3. **Database Migration**: Move your SQLite database between devices

## Troubleshooting

### Common Issues

#### "Poor OCR Results"
- **Problem**: Text not recognized correctly
- **Solutions**:
  - Ensure good lighting when photographing invoices
  - Keep the camera parallel to the invoice surface
  - Use flat, unwrinkled documents
  - Try the "Enhance Image" option before processing
  - Select the correct language in Settings

#### "Missing Line Items"
- **Problem**: Not all products/services detected
- **Solutions**:
  - Check if items are in tables vs. free-form lists
  - Try rotating the image 90° if the layout is vertical
  - Manually add missing items using the "Add Line Item" button
  - Adjust confidence thresholds to be more inclusive

#### "Slow Processing"
- **Problem**: Taking longer than expected
- **Solutions**:
  - Close other applications to free up CPU/RAM
  - Reduce image resolution if using very high-DPI scans
  - Process one page at a time for multi-page PDFs
  - Check that you're not running on battery saver mode

#### "Application Won't Start"
- **Problem**: Software fails to launch
- **Solutions**:
  - Check system requirements are met
  - Ensure antivirus isn't falsely flagging the application
  - Try running as administrator (Windows) or with sudo (Linux)
  - Look for error logs in `~/invoiceiq/logs/` or `%USERPROFILE%\invoiceiq\logs\`

### Getting Help
1. Check the FAQ section in Settings
2. Search the [GitHub Issues](https://github.com/your-org/invoiceiq/issues)
3. Visit the [Discussions](https://github.com/your-org/invoiceiq/discussions) forum
4. Contact support through the in-app help menu
5. For critical issues, email: support@invoiceiq.example.com

## Privacy & Security

### Data Handling
- **Local First**: All data remains on your device unless you choose to export
- **No Telemetry**: We don't collect usage data or analytics
- **No Cloud Dependencies**: Works 100% offline after initial setup
- **No Account Required**: Zero personal information needed to use the app

### Data Storage
- **Location**: SQLite database in your user directory:
  - Windows: `%APPDATA%\InvoiceIQ\invoiceiq.db`
  - macOS: `~/Library/Application Support/InvoiceIQ/invoiceiq.db`
  - Linux: `~/.local/share/InvoiceIQ/invoiceiq.db`
- **Encryption**: Consider enabling full-disk encryption on your device for additional protection
- **Backups**: Regularly export your data as JSON or CSV for safekeeping

### Permissions
The application only requests:
- **File Access**: To read your invoice files and save the database
- **Camera Access**: Only if you use the scan feature (can be denied)
- **Network Access**: Only for initial asset loading and optional update checks

### Security Best Practices
1. Keep your operating system updated
2. Use full-disk encryption (BitLocker, FileVault, LUKS)
3. Regularly backup your exported data
4. Be cautious when granting camera/file permissions
5. Consider using a dedicated user account for financial applications

## Accessibility Features

### Keyboard Navigation
- `Tab` / `Shift+Tab`: Navigate between fields
- `Enter`: Submit forms or activate buttons
- `Escape`: Close dialogs or cancel actions
- `Arrow Keys`: Navigate lists and menus
- `Ctrl+S`: Quick save (when in edit mode)

### Screen Reader Support
- Semantic HTML structure
- ARIA labels for interactive elements
- Live regions for dynamic content updates
- Skip navigation links

### Visual Accessibility
- High contrast mode toggle
- Adjustable text sizes (via browser zoom)
- Color-blind friendly palettes
- Focus indicators for keyboard users

## Frequently Asked Questions

### Q: Does InvoiceIQ require an internet connection?
A: No! After the initial download/installation, the application works 100% offline. Internet is only needed for:
- Downloading updates (optional)
- Fetching latest exchange rates (if using multi-currency features)
- Submitting bug reports or feature requests (optional)

### Q: How accurate is the OCR and data extraction?
A: Accuracy depends on invoice quality:
- Clear, printed invoices: 90-95% accuracy
- Handwritten or poor quality scans: 70-85% accuracy
- You can always review and correct extracted data before saving

### Q: Can I process invoices in languages other than English?
A: Yes! InvoiceIQ supports multiple languages through Tesseract OCR:
- Go to Settings → OCR Languages
- Select your preferred language(s)
- Note: Additional language packs may increase processing time slightly

### Q: Is there a limit to how many invoices I can store?
A: No hard limit - the only constraint is your available storage space.
Typical usage: 10,000 invoices ≈ 50-100MB database size

### Q: Can I use InvoiceIQ for business accounting?
A: Yes! Many small businesses and freelancers use InvoiceIQ for:
- Expense tracking
- Tax preparation documentation
- Client invoicing records
- Reimbursement tracking
Consult with your accountant for specific compliance requirements in your jurisdiction.

### Q: How does the "learning" feature work?
A: When you correct a category for a specific vendor, InvoiceIQ remembers:
- Vendor name (normalized for matching)
- Your selected category
- Future invoices from similar-named vendors will suggest your choice
- You can view and manage these learned associations in Settings

---

## Getting Help & Updates

### Finding Help
- **In-App Help**: Click the question mark icon in the top-right corner
- **Documentation**: This user manual is also available offline in the app
- **Community Forum**: [github.com/your-org/invoiceiq/discussions](https://github.com/your-org/invoiceiq/discussions)
- **Issue Tracker**: [github.com/your-org/invoiceiq/issues](https://github.com/your-org/invoiceiq/issues)

### Staying Updated
- **Desktop App**: Automatic update notifications when available
- **Web Version**: Always running the latest code when you refresh
- **Manual Updates**: Check the [Releases page](https://github.com/your-org/invoiceiq/releases)
- **Release Notes**: See what's new in each version

### Reporting Issues
When encountering problems:
1. Try restarting the application
2. Check if the issue persists with different invoice samples
3. Collect relevant information:
   - Screenshots or screen recordings
   - Console logs (Developer Tools → Console)
   - Steps to reproduce
   - Your OS and version
4. Submit via the in-app "Report Issue" feature or GitHub

---

## Appendix

### Glossary of Terms
- **OCR**: Optical Character Recognition - technology that converts images of text into machine-readable text
- **PWA**: Progressive Web App - a web application that can be installed and used like a native app
- **SPA**: Single Page Application - a web app that loads a single HTML page and dynamically updates content
- **CSV**: Comma-Separated Values - a simple file format for tabular data
- **JSON**: JavaScript Object Notation - a lightweight data interchange format

### Keyboard Shortcuts Reference
| Action | Shortcut |
|--------|----------|
| New Invoice | `Ctrl+N` |
| Save | `Ctrl+S` |
| Delete Selected | `Delete` |
| Search Focus | `/` |
| Next Field | `Tab` |
| Previous Field | `Shift+Tab` |
| Cancel/Close | `Escape` |
| Help Toggle | `F1` or `?` |
| Fullscreen Toggle | `F11` |

### Supported Countries & Formats
While InvoiceIQ works globally, it's particularly optimized for:
- **North America**: US invoices, Canadian GST/HST
- **Europe**: EU VAT formats, UK invoices
- **Asia**: Japanese consumption tax, Indian GST
- **Australia/New Zealand**: GST formats
- **Latin America**: Various VAT/IVA systems

Date formats are automatically detected based on locale settings, but can be manually adjusted in the edit form if needed.

---

*Last Updated: July 2024*  
*Version: 1.0.0*  
*© 2024 InvoiceIQ Team. All rights reserved.*