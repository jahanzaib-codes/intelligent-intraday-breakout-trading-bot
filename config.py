"""
Configuration file for the Intelligent Intraday Breakout Trading Bot
Contains all settings, parameters, and constants
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==================== API KEYS & CREDENTIALS ====================
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Interactive Brokers credentials
IB_HOST = os.getenv('IB_HOST', '127.0.0.1')
IB_PORT = int(os.getenv('IB_PORT', '7497'))  # 7497 for TWS, 4001 for Gateway
IB_CLIENT_ID = int(os.getenv('IB_CLIENT_ID', '1'))

# ==================== STOCK SCREENING FILTERS ====================
SCREENER_CONFIG = {
    'region': 'United States',
    'exchange': 'NASDAQ',
    'price_min': 0.30,
    'price_max': 5.00,
    'change_min': 2.0,  # 2%
    'change_max': 300.0,  # 300%
    'volume_multiplier': 1.5,  # 1.5x average volume
    'market_cap_min': 10_000_000,  # $10M
    'market_cap_max': 3_000_000_000,  # $3B
    'rsi_min': 50,
    'rsi_max': 80,
    'momentum_filter': True,  # price * volume > market_cap
}

# ==================== TECHNICAL INDICATORS ====================
TECHNICAL_CONFIG = {
    'rsi_period': 14,
    'bollinger_period': 20,
    'bollinger_std': 2,
    'volatility_period': 5,  # minutes
    'green_candle_period': 20,
    'breakout_period': 20,
    'ema_short': 5,
    'ema_long': 10,
}

# ==================== ENTRY CONDITIONS ====================
ENTRY_CONDITIONS = {
    'price_range_min': 0.30,
    'price_range_max': 5.00,
    'volume_surge_min': 1.5,
    'rsi_min': 50,
    'bollinger_width_min': 0.05,
    'green_candle_ratio_min': 0.60,  # 60%
    'volatility_min': 0.02,  # 2%
    'price_change_min': 2.0,  # 2%
    'price_change_max': 100.0,  # 100%
    'ai_score_min': 70,
}

# ==================== TRADING PARAMETERS ====================
TRADING_CONFIG = {
    'limit_order_discount': 0.0075,  # 0.75% below current price
    'max_position_size': 0.02,  # 2% of portfolio per trade
    'max_positions': 5,  # maximum concurrent positions
}

# ==================== STOP LOSS TIERS ====================
STOP_LOSS_TIERS = {
    1.0: 0.05,   # <$1: 5%
    3.0: 0.04,   # <$3: 4%
    5.0: 0.03,   # <$5: 3%
}

# ==================== PROFIT TARGETS ====================
PROFIT_TARGETS = {
    'target_1': 0.10,  # 10% gain
    'target_2': 0.25,  # 25% gain
    'trailing_stop_percent': 0.05,  # 5% trailing stop
}

# ==================== MARKET TIMING ====================
MARKET_TIMING = {
    'start_time': '09:30',  # ET
    'end_time': '15:20',    # ET
    'close_time': '15:50',  # ET - close all positions
    'timezone': 'US/Eastern',
}

# ==================== MONITORING ====================
MONITORING_CONFIG = {
    'price_check_interval': 60,  # seconds
    'pnl_summary_interval': 900,  # 15 minutes
    'log_level': 'INFO',
}

# ==================== AI MODEL ====================
AI_CONFIG = {
    'model_path': 'models/xgboost_model.pkl',
    'features': [
        'price', 'volume', 'avg_volume', 'green_ratio', 'rsi',
        'boll_width', 'volatility', 'breakout', 'market_cap',
        'ma10', 'ma30', 'change_percent'
    ],
    'threshold': 70,
}

# ==================== LOGGING ====================
LOGGING_CONFIG = {
    'log_file': 'logs/trading_bot.log',
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5,
} 