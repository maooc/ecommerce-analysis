import pandas as pd
import numpy as np
from datetime import datetime

def load_sales_data(file_path='data/sales_data.csv'):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def calculate_revenue_metrics(df):
    total_revenue = df['total_amount'].sum()
    avg_order_value = df['total_amount'].mean()
    median_order_value = df['total_amount'].median()
    
    return {
        'total_revenue': total_revenue,
        'avg_order_value': avg_order_value,
        'median_order_value': median_order_value,
        'total_orders': len(df)
    }

def analyze_by_category(df):
    category_stats = df.groupby('product_category').agg({
        'total_amount': ['sum', 'mean', 'count'],
        'quantity': 'sum'
    }).round(2)
    
    category_stats.columns = ['total_revenue', 'avg_order_value', 'order_count', 'total_quantity']
    category_stats = category_stats.sort_values('total_revenue', ascending=False)
    
    return category_stats

def analyze_by_region(df):
    region_stats = df.groupby('region').agg({
        'total_amount': ['sum', 'mean', 'count'],
        'quantity': 'sum'
    }).round(2)
    
    region_stats.columns = ['total_revenue', 'avg_order_value', 'order_count', 'total_quantity']
    region_stats = region_stats.sort_values('total_revenue', ascending=False)
    
    return region_stats

def analyze_by_payment_method(df):
    payment_stats = df.groupby('payment_method').agg({
        'total_amount': ['sum', 'mean', 'count']
    }).round(2)
    
    payment_stats.columns = ['total_revenue', 'avg_order_value', 'order_count']
    payment_stats = payment_stats.sort_values('total_revenue', ascending=False)
    
    return payment_stats

def calculate_top_products(df, top_n=10):
    product_stats = df.groupby('product_name').agg({
        'total_amount': 'sum',
        'quantity': 'sum',
        'order_id': 'count'
    }).round(2)
    
    product_stats.columns = ['total_revenue', 'total_quantity', 'order_count']
    product_stats = product_stats.sort_values('total_revenue', ascending=False)
    
    return product_stats.head(top_n)

def calculate_top_customers(df, top_n=5):
    customer_stats = df.groupby('customer_id').agg({
        'total_amount': 'sum',
        'order_id': 'count'
    }).round(2)
    
    customer_stats.columns = ['total_spent', 'order_count']
    customer_stats = customer_stats.sort_values('total_spent', ascending=False)
    
    return customer_stats.head(top_n)

def calculate_daily_trend(df):
    daily_sales = df.groupby('date').agg({
        'total_amount': 'sum',
        'order_id': 'count'
    }).round(2)
    
    daily_sales.columns = ['daily_revenue', 'order_count']
    daily_sales = daily_sales.sort_index()
    
    return daily_sales

def calculate_category_distribution(df):
    category_dist = df.groupby('product_category')['total_amount'].sum()
    category_percentages = (category_dist / category_dist.sum() * 100).round(2)
    return category_percentages.to_dict()

def calculate_conversion_metrics(df):
    unique_customers = df['customer_id'].nunique()
    total_orders = len(df)
    orders_per_customer = total_orders / unique_customers if unique_customers > 0 else 0
    
    return {
        'unique_customers': unique_customers,
        'total_orders': total_orders,
        'orders_per_customer': round(orders_per_customer, 2)
    }

def perform_rfm_analysis(df):
    if df.empty or 'date' not in df.columns:
        return pd.DataFrame(columns=['customer_id', 'recency', 'frequency', 'monetary', 'R_score', 'F_score', 'M_score'])
    
    valid_dates = df['date'].dropna()
    if valid_dates.empty:
        return pd.DataFrame(columns=['customer_id', 'recency', 'frequency', 'monetary', 'R_score', 'F_score', 'M_score'])
    
    snapshot_date = valid_dates.max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('customer_id').agg({
        'date': lambda x: (snapshot_date - x.max()).days,
        'order_id': 'count',
        'total_amount': 'sum'
    }).reset_index()
    
    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']
    
    rfm['R_score'] = pd.qcut(rfm['recency'], q=5, labels=[5, 4, 3, 2, 1], duplicates='drop')
    rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    rfm['M_score'] = pd.qcut(rfm['monetary'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    
    return rfm

def analyze_time_patterns(df):
    df['day_of_week'] = df['date'].dt.dayofweek
    df['hour'] = df['date'].dt.hour
    
    dow_stats = df.groupby('day_of_week')['total_amount'].mean()
    dow_stats.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    return dow_stats.to_dict()

def generate_insights(df):
    insights = []
    
    total_revenue = df['total_amount'].sum()
    category_stats = analyze_by_category(df)
    top_category = category_stats.index[0]
    top_category_revenue = category_stats.iloc[0]['total_revenue']
    
    insights.append({
        'type': 'revenue',
        'message': f"Total revenue: ${total_revenue:,.2f}"
    })
    
    insights.append({
        'type': 'category',
        'message': f"Top category: {top_category} (${top_category_revenue:,.2f})"
    })
    
    region_stats = analyze_by_region(df)
    top_region = region_stats.index[0]
    insights.append({
        'type': 'region',
        'message': f"Top region: {top_region}"
    })
    
    return insights

def perform_comprehensive_analysis(df):
    results = {
        'revenue_metrics': calculate_revenue_metrics(df),
        'category_analysis': analyze_by_category(df),
        'region_analysis': analyze_by_region(df),
        'payment_analysis': analyze_by_payment_method(df),
        'top_products': calculate_top_products(df),
        'top_customers': calculate_top_customers(df),
        'daily_trend': calculate_daily_trend(df),
        'category_distribution': calculate_category_distribution(df),
        'conversion_metrics': calculate_conversion_metrics(df),
        'time_patterns': analyze_time_patterns(df),
        'insights': generate_insights(df)
    }
    
    return results

if __name__ == '__main__':
    df = load_sales_data()
    print(f"Loaded {len(df)} orders")
    
    results = perform_comprehensive_analysis(df)
    
    print("\nRevenue Metrics:")
    for key, value in results['revenue_metrics'].items():
        print(f"  {key}: {value}")
    
    print("\nTop Products:")
    print(results['top_products'])
