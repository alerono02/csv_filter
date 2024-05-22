from datetime import datetime

import pandas as pd


def load_data(filename: str) -> pd.DataFrame:
    data = pd.read_csv(filename)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data


def count_actions(data: pd.DataFrame) -> pd.DataFrame:
    client_actions = data.groupby('client_id')['action'].count().reset_index(name='action_count')
    return client_actions


def filter_data(data: pd.DataFrame, column: str, filter_param: str) -> pd.DataFrame:
    if data.dtypes[column] == 'int64':
        filtered_data = data[data[column] == int(filter_param)]
    elif data.dtypes[column] == 'datetime[ns]':
        filtered_data = data[data[column] == datetime.strptime(filter_param, '%y/%m/%d %H:%M:%S')]
    else:
        filtered_data = data[data[column] == filter_param]
    return filtered_data


def analyze_client_behavior(data: pd.DataFrame):
    client_actions = count_actions(data)
    average_actions = client_actions['action_count'].mean()

    top_clients = client_actions.nlargest(5, 'action_count')

    analysis_results = {
        'average_actions': average_actions,
        'top_clients': top_clients.to_dict(orient='records')
    }

    return pd.DataFrame(analysis_results)


def save_data(data: pd.DataFrame, filename: str, format_file: str):
    match format_file.lower():
        case 'csv':
            data.to_csv(f'{filename}.csv', index=False)
            print(f'Saved to {filename}.csv')
        case 'excel':
            data.to_excel(f'{filename}.xlsx', index=False)
            print(f'Saved to {filename}.xlsx')
        case 'xml':
            data.to_xml(f'{filename}.xml', index=False)
            print(f'Saved to {filename}.xml')
        case 'json':
            data.to_json(f'{filename}.json', index=False)
            print(f'Saved to {filename}.json')
        case _:
            raise ValueError(f'Invalid format: {format_file}')