# Intelligent Intraday Breakout Trading Bot

A fully automated trading bot that identifies and executes high-momentum breakout trades during intraday sessions on NASDAQ using real-time data, smart technical filtering, and AI (XGBoost model) — with order execution via IB Gateway and real-time Telegram alerts.

## 🚀 Features

### Stock Screening
- **Real-time NASDAQ screening** with Webull-style filters
- **Price range**: $0.30 to $5.00
- **Volume surge**: ≥ 1.5× average volume (3-month)
- **Market cap**: $10M to $3B
- **RSI**: between 50 and 80
- **Momentum filter**: Dollar volume > Market cap

### Technical Analysis
- **RSI** (Relative Strength Index)
- **Bollinger Bands Width** for volatility measurement
- **5-minute volatility** calculation
- **Green candle ratio** (last 20 candles)
- **Breakout detection** from recent resistance
- **Moving averages** (MA10, MA30, EMA5, EMA10)

### AI Prediction
- **XGBoost model** for trade success prediction
- **Feature engineering** from technical indicators
- **Probability scoring** (0-100)
- **Threshold-based filtering** (≥70 score required)

### Risk Management
- **Dynamic stop-losses** based on price tiers:
  - <$1: 5%
  - <$3: 4%
  - <$5: 3%
- **Profit targets**:
  - Target 1 (10%): Move stop to entry
  - Target 2 (25%): Move stop to +10%
  - Target 3+: Enable trailing stop (5%)
- **Position sizing**: 2% of portfolio per trade
- **Maximum positions**: 5 concurrent trades

### Market Timing
- **Trading hours**: 9:30 AM - 3:20 PM ET
- **Position closure**: 3:50 PM ET (10 min before close)
- **Weekend trading**: Disabled

### Notifications
- **Real-time Telegram alerts** for:
  - Buy order executions
  - Sell triggers (stop-loss/target)
  - Stop-loss updates
  - Profit target achievements
  - P&L summaries (every 15 minutes)
  - Error alerts

## 📁 Project Structure

```
riyadh64/
├── main.py                 # Main entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables template
├── README.md             # This file
├── src/                  # Source code
│   ├── __init__.py
│   ├── main_bot.py       # Main bot orchestrator
│   ├── data/             # Data handling
│   │   ├── __init__.py
│   │   └── stock_screener.py
│   ├── analysis/         # Technical analysis
│   │   ├── __init__.py
│   │   └── technical_indicators.py
│   ├── ai/               # AI model
│   │   ├── __init__.py
│   │   └── prediction_model.py
│   ├── trading/          # Trading logic
│   │   ├── __init__.py
│   │   └── risk_management.py
│   └── notifications/    # Notifications
│       ├── __init__.py
│       └── telegram_notifier.py
├── models/               # AI model files
├── logs/                 # Log files
└── data/                 # Data storage
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Interactive Brokers Gateway 10.38 (for live trading)
- Telegram Bot Token (for notifications)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd riyadh64
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp env_example.txt .env
   # Edit .env with your credentials
   ```

4. **Set up Telegram Bot**
   - Create a bot via @BotFather on Telegram
   - Get your bot token and chat ID
   - Add to `.env` file

5. **Configure Interactive Brokers** (for live trading)
   - Install IB Gateway 10.38
   - Configure connection settings in `.env`
   - Enable API connections in TWS/Gateway

## ⚙️ Configuration

### Environment Variables (.env)
```bash
# Telegram Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

# Interactive Brokers Configuration
IB_HOST=127.0.0.1
IB_PORT=7497
IB_CLIENT_ID=1
```

### Key Configuration Parameters (config.py)
- **Screening filters**: Price range, volume, market cap, RSI
- **Technical indicators**: Periods, thresholds
- **Risk management**: Stop-loss tiers, position sizing
- **Market timing**: Trading hours, timezone
- **AI model**: Features, threshold, model path

## 🚀 Usage

### Running the Bot

1. **Start the bot**
   ```bash
   python main.py
   ```

2. **Monitor via Telegram**
   - Bot will send startup notification
   - Real-time alerts for all trading activities
   - P&L summaries every 15 minutes

3. **Check logs**
   ```bash
   tail -f logs/trading_bot.log
   ```

### Bot Controls

The bot runs automatically during market hours. For manual control:

```python
from src.main_bot import TradingBot

bot = TradingBot()

# Start bot
bot.start()

# Pause trading
bot.pause()

# Resume trading
bot.resume()

# Stop bot
bot.stop()

# Get status
status = bot.get_status()
```

## 📊 Trading Strategy

### Entry Conditions
All of the following must be met:
- ✅ Price between $0.30-$5.00
- ✅ Volume surge ≥ 1.5× average
- ✅ RSI > 50
- ✅ Bollinger Band Width > 0.05
- ✅ Green candle ratio ≥ 60%
- ✅ Breakout above recent resistance
- ✅ 5-min volatility ≥ 2%
- ✅ AI Score ≥ 70

### Exit Conditions
- **Stop-loss**: Dynamic based on price tier
- **Profit targets**: 10% and 25% gains
- **Trailing stop**: 5% after 25% target
- **End of day**: All positions closed at 3:50 PM ET

## 🤖 AI Model

### Features Used
- Price, volume, average volume
- RSI, Bollinger Band width, volatility
- Green candle ratio, breakout detection
- Moving averages, market cap
- Price change percentage

### Model Training
- **Algorithm**: XGBoost Classifier
- **Features**: 12 technical indicators
- **Output**: Probability score (0-100)
- **Threshold**: 70% minimum for trade entry

### Model Management
- Automatic model loading/saving
- Dummy model creation for testing
- Retraining capabilities
- Model performance monitoring

## 📈 Performance Monitoring

### Real-time Metrics
- Active positions count
- Total portfolio value
- Unrealized P&L
- Average P&L percentage
- Position history

### Logging
- Comprehensive logging to `logs/trading_bot.log`
- Error tracking and notifications
- Performance analytics
- Debug information

## 🔧 Customization

### Adding New Indicators
1. Add calculation in `technical_indicators.py`
2. Update feature list in `config.py`
3. Retrain AI model with new features

### Modifying Risk Parameters
1. Edit `STOP_LOSS_TIERS` in `config.py`
2. Adjust `PROFIT_TARGETS`
3. Modify position sizing rules

### Changing Screening Criteria
1. Update `SCREENER_CONFIG` in `config.py`
2. Modify filter logic in `stock_screener.py`
3. Test with historical data

## ⚠️ Risk Disclaimer

**This software is for educational and research purposes only. Trading involves substantial risk of loss and is not suitable for all investors. Past performance does not guarantee future results.**

### Important Notes
- Always test thoroughly in paper trading mode
- Start with small position sizes
- Monitor the bot continuously
- Have proper risk management in place
- Understand all trading strategies before live deployment

## 🐛 Troubleshooting

### Common Issues

1. **Telegram notifications not working**
   - Check bot token and chat ID
   - Verify internet connection
   - Test with `notifier.test_connection()`

2. **No stocks passing screener**
   - Check market hours
   - Verify data sources
   - Adjust screening criteria

3. **AI model errors**
   - Ensure XGBoost is installed
   - Check model file path
   - Verify feature compatibility

4. **Performance issues**
   - Monitor system resources
   - Check API rate limits
   - Optimize data fetching

### Debug Mode
Enable debug logging in `config.py`:
```python
MONITORING_CONFIG = {
    'log_level': 'DEBUG',
    # ... other settings
}
```

## 📞 Support

For issues and questions:
1. Check the logs in `logs/trading_bot.log`
2. Review configuration settings
3. Test individual components
4. Consult documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔄 Version History

- **v1.0.0**: Initial release with core functionality
  - Stock screening and technical analysis
  - AI prediction model
  - Risk management system
  - Telegram notifications
  - Market timing controls

---

**Happy Trading! 🚀📈** 