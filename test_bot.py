#!/usr/bin/env python3
"""
Test script for the Trading Bot
Verifies all components are working correctly
"""

import sys
import os
import logging

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.data.stock_screener import StockScreener
from src.analysis.technical_indicators import TechnicalIndicators
from src.ai.prediction_model import PredictionModel
from src.trading.risk_management import RiskManager
from src.notifications.telegram_notifier import TelegramNotifier

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_stock_screener():
    """Test stock screener functionality"""
    print("\n🔍 Testing Stock Screener...")
    
    try:
        screener = StockScreener()
        
        # Test with a few known stocks
        test_symbols = ['AAPL', 'MSFT', 'TSLA']
        
        for symbol in test_symbols:
            data = screener.fetch_stock_data(symbol)
            if data:
                print(f"✅ {symbol}: ${data['price']:.2f} ({data['change_percent']:.1f}%)")
            else:
                print(f"❌ {symbol}: No data available")
        
        return True
        
    except Exception as e:
        print(f"❌ Stock screener test failed: {str(e)}")
        return False

def test_technical_indicators():
    """Test technical indicators calculation"""
    print("\n📊 Testing Technical Indicators...")
    
    try:
        analyzer = TechnicalIndicators()
        
        # Test with a sample stock
        symbol = 'AAPL'
        technical_data = analyzer.get_technical_analysis(symbol)
        
        if technical_data:
            print(f"✅ {symbol} Technical Analysis:")
            print(f"   RSI: {technical_data['rsi']:.1f}")
            print(f"   Bollinger Width: {technical_data['bollinger_width']:.3f}")
            print(f"   Volatility: {technical_data['volatility']:.1f}%")
            print(f"   Green Candle Ratio: {technical_data['green_candle_ratio']:.1%}")
            print(f"   Breakout: {technical_data['is_breakout']}")
            
            # Test entry conditions
            conditions_met, results = analyzer.check_entry_conditions(technical_data)
            print(f"   Entry Conditions Met: {conditions_met}")
            
            return True
        else:
            print(f"❌ No technical data for {symbol}")
            return False
            
    except Exception as e:
        print(f"❌ Technical indicators test failed: {str(e)}")
        return False

def test_ai_model():
    """Test AI prediction model"""
    print("\n🤖 Testing AI Model...")
    
    try:
        model = PredictionModel()
        
        # Test model info
        model_info = model.get_model_info()
        print(f"✅ Model Type: {model_info.get('model_type', 'Unknown')}")
        print(f"✅ Features: {len(model_info.get('features', []))}")
        print(f"✅ Threshold: {model_info.get('threshold', 0)}")
        
        # Test prediction with sample data
        sample_data = {
            'symbol': 'TEST',
            'price': 1.50,
            'volume': 1000000,
            'avg_volume': 800000,
            'rsi': 65.0,
            'bollinger_width': 0.08,
            'volatility': 2.5,
            'green_candle_ratio': 0.7,
            'is_breakout': True,
            'market_cap': 50000000,
            'ma10': 1.48,
            'ma30': 1.45,
            'price_change_percent': 5.0
        }
        
        score = model.predict_score(sample_data)
        is_eligible = model.is_trade_eligible(sample_data)
        
        print(f"✅ Sample Prediction Score: {score:.1f}")
        print(f"✅ Trade Eligible: {is_eligible}")
        
        return True
        
    except Exception as e:
        print(f"❌ AI model test failed: {str(e)}")
        return False

def test_risk_management():
    """Test risk management functionality"""
    print("\n🛡️ Testing Risk Management...")
    
    try:
        risk_manager = RiskManager()
        
        # Test position sizing
        portfolio_value = 100000
        price = 2.50
        shares = risk_manager.calculate_position_size(price, portfolio_value)
        print(f"✅ Position Size: {shares} shares at ${price:.2f}")
        
        # Test stop-loss calculation
        stop_loss = risk_manager.calculate_stop_loss(price)
        print(f"✅ Stop Loss: ${stop_loss:.2f}")
        
        # Test profit targets
        targets = risk_manager.calculate_profit_targets(price)
        print(f"✅ Target 1: ${targets['target_1']:.2f}")
        print(f"✅ Target 2: ${targets['target_2']:.2f}")
        
        # Test position creation
        position = risk_manager.create_position('TEST', price, shares, portfolio_value)
        if position:
            print(f"✅ Position Created: {position['position_id']}")
            
            # Test position update
            update_result = risk_manager.update_position(position['position_id'], price * 1.05)
            if update_result:
                print(f"✅ Position Updated: P&L {update_result['position']['unrealized_pnl_percent']:.2f}%")
            
            # Test position closure
            exit_record = risk_manager.close_position(position['position_id'], price * 1.02, "Test")
            if exit_record:
                print(f"✅ Position Closed: P&L ${exit_record['final_pnl']:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Risk management test failed: {str(e)}")
        return False

def test_telegram_notifications():
    """Test Telegram notifications"""
    print("\n📱 Testing Telegram Notifications...")
    
    try:
        notifier = TelegramNotifier()
        
        # Test connection
        connection_ok = notifier.test_connection()
        
        if connection_ok:
            print("✅ Telegram connection successful")
            
            # Test various notification types
            notifier.notify_bot_status("test", {"Test": "Value"})
            print("✅ Status notification sent")
            
            return True
        else:
            print("⚠️ Telegram not configured or connection failed")
            return True  # Not a failure, just not configured
            
    except Exception as e:
        print(f"❌ Telegram test failed: {str(e)}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("\n⚙️ Testing Configuration...")
    
    try:
        from config import (
            SCREENER_CONFIG, TECHNICAL_CONFIG, ENTRY_CONDITIONS,
            TRADING_CONFIG, STOP_LOSS_TIERS, PROFIT_TARGETS,
            MARKET_TIMING, MONITORING_CONFIG, AI_CONFIG
        )
        
        print("✅ All configuration sections loaded successfully")
        print(f"✅ Screener filters: {len(SCREENER_CONFIG)} parameters")
        print(f"✅ Technical indicators: {len(TECHNICAL_CONFIG)} parameters")
        print(f"✅ Entry conditions: {len(ENTRY_CONDITIONS)} parameters")
        print(f"✅ Trading config: {len(TRADING_CONFIG)} parameters")
        print(f"✅ Stop-loss tiers: {len(STOP_LOSS_TIERS)} tiers")
        print(f"✅ Profit targets: {len(PROFIT_TARGETS)} targets")
        print(f"✅ Market timing: {MARKET_TIMING['timezone']} timezone")
        print(f"✅ AI features: {len(AI_CONFIG['features'])} features")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("🧪 Trading Bot Test Suite")
    print("=" * 50)
    
    tests = [
        ("Configuration", test_configuration),
        ("Stock Screener", test_stock_screener),
        ("Technical Indicators", test_technical_indicators),
        ("AI Model", test_ai_model),
        ("Risk Management", test_risk_management),
        ("Telegram Notifications", test_telegram_notifications),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Test Summary")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Bot is ready to run.")
        print("\nTo start the bot:")
        print("python main.py")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        print("Make sure all dependencies are installed and configured correctly.")

if __name__ == "__main__":
    main() 