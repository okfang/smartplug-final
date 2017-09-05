device_data = {
    "device_id":1,
    "year_detail": {
        "err_code": 0,
        "month_list": [
            {
                "month": 8,
                "energy": 0,
                "year": 2017
            }
        ]
    },
    "timezone": {
        "index": 5,
        "err_code": 0,
        "dst_offset": 0,
        "tz_str": "PST8",
        "zone_str": "(UTC-08:00) Pacific Standard Time (US & Canada)"
    },
    "time": {
        "min": 7,
        "err_code": 0,
        "wday": 3,
        "sec": 44,
        "mday": 30,
        "month": 8,
        "year": 2017,
        "hour": 18
    },
    "power_current": {
        "total": 0,
        "current": 0.027499,
        "power": 0,
        "err_code": 0,
        "voltage": 221.514712
    },
    "mon_detail": {
        "err_code": 0,
        "day_list": [
            {
                "month": 8,
                "energy": 4,
                "year": 2017,
                "day": 28
            },
            {
                "month": 8,
                "energy": 0,
                "year": 2017,
                "day": 29
            },
            {
                "month": 8,
                "energy": 0,
                "year": 2017,
                "day": 30
            }
        ]
    },
    "sysinfo": {
        "model": "HS110(UK)",
        "dev_name": "Wi-Fi Smart Plug With Energy Monitoring",
        "alias": "dev_for_test",
        "mac": "50:C7:BF:5B:26:7B",
        "fwId": "9176FB9731E6D84BD775BCF6BBD742EF",
        "type": "IOT.SMARTPLUGSWITCH",
        "updating": 0,
        "on_time": 0,
        "err_code": 0,
        "icon_hash": "",
        "hw_ver": "1.0",
        "longitude": 0,
        "feature": "TIM:ENE",
        "latitude": 0,
        "rssi": -28,
        "active_mode": "none",
        "hwId": "2448AB56FB7E126DE5CF876F84C6DEB5",
        "sw_ver": "1.0.10 Build 160316 Rel.181342",
        "oemId": "90AEEA7AECBF1A879FCA3C104C58C4D8",
        "led_off": 0,
        "relay_state": 0,
        "deviceId": "8006486ECAF3B37296EE562F3E413D10187823FA"
    }
}


line_chart_data = {
        'labels' : ['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00'],
        'datasets' :[
                    {  'label' : 'Total', 'backgroundColor' : '#00FF00', 'borderColor' : 'palette.transparent', 'data' : [
                    '0.1', '0.2', '3.1', '4.5', '5.8', '1.2', '1.1']},
                    {'label' : 'Light', 'backgroundColor' : '#FF0000', 'borderColor' : 'palette.transparent', 'data' : [
                    '1', '2', '3', '4', '3', '2', '1']},
                    {'label' : 'Computer', 'backgroundColor' : '#7D26CD', 'borderColor' : 'palette.transparent', 'data' : [
                    '5', '4', '3', '2', '1', '4', '5']}
        ]
    }

pipe_chart_data = {
        'labels': ['Light', 'Computers', 'Television', 'Refrige', 'Air-Conditioner', 'Micro-wave', 'Fans'],
        'datasets': {
            'label': '颜色们',
            'backgroundColor': ['#FF0000', '#00FF00', '#C0FFEE', '#EEFF0C', '#ABCDEE',
                                '#BCDEEF', '#BEEFEE'],
            'data': ['0.4', '0.2', '3.1', '8', '5.8', '1.2', '2.0']
        }
    }

plugs_data = [{'name' :'plug1' ,'id':'asdkfbee33','type':'what?','description':'天王盖地虎','consumption':'100kwh'},
            {'name' :'plug2' ,'id':'asdkfbee33','type':'what?','description':'宝塔镇河妖','consumption':'122kwh'},
            {'name' :'plug3' ,'id':'asdkfbee33','type':'what?','description':'左青龙右白虎','consumption':'233kwh'}
    ]

map_data = {
        'ViewX' : '58.404',
        'ViewY' : '15.598',
        'ViewScale' : '16',
        'MyposX' : '58.4042552',
        'MyposY' : '15.5989675',
        'MyInfo' : 'I am here',
        0:{'posX': '58.40425', 'posY': '15.59896', 'Rad': '12', 'FillOpcity': '0.4', 'FillColor': '#F00000',
             'Info': 'color:#F00000'},
        1:{'posX': '58.40436', 'posY': '15.59895', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F20000',
             'Info': 'color:#F20000'},
        2:{'posX': '58.40447', 'posY': '15.59893', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F40000',
             'Info': 'color:#F40000'},
        3:{'posX': '58.40424', 'posY': '15.59894', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F60000',
             'Info': 'color:#F60000'},
        4:{'posX': '58.40453', 'posY': '15.59894', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#F80000',
             'Info': 'color:#F80000'},
        5:{'posX': '58.40410', 'posY': '15.59892', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#FA0000',
             'Info': 'color:#FA0000'},
        6:{'posX': '58.40481', 'posY': '15.59891', 'Rad': '10', 'FillOpcity': '0.4', 'FillColor': '#FC0000',
             'Info': 'color:#FC0000'}
    }