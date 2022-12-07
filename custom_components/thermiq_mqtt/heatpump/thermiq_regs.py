# ThermIQ generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4
FIELD_BITMASK = 3


# Register as sensors
reg_id = {
#  reg_id          : ['reg#', 'type', 'unit', 'bitmask or min', 'max', 'panel', panel_order' ],
  'outdoor_t'                    : ['r00', 'temperature',            'ºC',               '',      '',  2,  1  ],
  'indoor_t'                     : ['r01', 'temperature',            'ºC',               '',      '',  2,  2  ],
  'indoor_dec_t'                 : ['r02', 'temperature',            '0.1C',              '',      '',  0,  0  ],
  'indoor_target_t'              : ['r03', 'temperature',            'ºC',               '',      '',  0,  0  ],
  'indoor_target_dec_t'          : ['r04', 'temperature',            '0.1C',              '',      '',  0,  0  ],
  'supplyline_t'                 : ['r05', 'temperature',            'ºC',               '',      '',  2,  3  ],
  'returnline_t'                 : ['r06', 'temperature',            'ºC',               '',      '',  2,  4  ],
  'boiler_t'                     : ['r07', 'temperature',            'ºC',               '',      '',  2,  5  ],
  'brine_out_t'                  : ['r08', 'temperature',            'ºC',               '',      '',  2,  7  ],
  'brine_in_t'                   : ['r09', 'temperature',            'ºC',               '',      '',  2,  8  ],
  'cooling_t'                    : ['r0a', 'temperature',            'ºC',               '',      '',  2, 10  ],
  'supply_shunt_t'               : ['r0b', 'temperature',            'ºC',               '',      '',  2,  9  ],
  'current_consumed_a'           : ['r0c', 'sensor',                 'A',                 '',      '',  0,  0  ],
  'boiler_3kw_on'                : ['r0d', 'binary_sensor',          '',             0x0001,     -1,  0,  0   ],
  'boiler_6kw_on'                : ['r0d', 'binary_sensor',          '',             0x0002,     -1,  0,  0   ],
  'supplyline_target_t'          : ['r0e', 'temperature',            'ºC',               '',      '',  0,  0  ],
  'supplyline_shunt_target_t'    : ['r0f', 'temperature',            'ºC',               '',      '',  0,  0  ],
  'brine_pump_on'                : ['r10', 'binary_sensor',          '',             0x0001,     -1,  0,  0   ],
  'compressor_on'                : ['r10', 'binary_sensor',          '',             0x0002,     -1,  0,  0   ],
  'supply_pump_on'               : ['r10', 'binary_sensor',          '',             0x0004,     -1,  0,  0   ],
  'hotwaterproduction_on'        : ['r10', 'binary_sensor',          '',             0x0008,     -1,  0,  0   ],
  'aux2_heating_on'              : ['r10', 'binary_sensor',          '',             0x0010,     -1,  0,  0   ],
  'shunt1_n'                     : ['r10', 'binary_sensor',          '',             0x0020,     -1,  0,  0   ],
  'shunt1_p'                     : ['r10', 'binary_sensor',          '',             0x0040,     -1,  0,  0   ],
  'aux1_heating_on'              : ['r10', 'binary_sensor',          '',             0x0080,     -1,  0,  0   ],
  'shunt2_n'                     : ['r11', 'binary_sensor',          '',             0x0001,     -1,  0,  0   ],
  'shunt2_p'                     : ['r11', 'binary_sensor',          '',             0x0002,     -1,  0,  0   ],
  'shunt_cooling_n'              : ['r11', 'binary_sensor',          '',             0x0004,     -1,  0,  0   ],
  'shunt_cooling_p'              : ['r11', 'binary_sensor',          '',             0x0008,     -1,  0,  0   ],
  'active_cooling_on'            : ['r11', 'binary_sensor',          '',             0x0010,     -1,  0,  0   ],
  'passive_cooling_on'           : ['r11', 'binary_sensor',          '',             0x0020,     -1,  0,  0   ],
  'alarm_indication_on'          : ['r11', 'binary_sensor',          '',             0x0040,     -1,  0,  0   ],
  'pwm_out_period'               : ['r12', 'sensor',                 '%',                 '',      '',  0,  0  ],
  'highpressure_alm'             : ['r13', 'binary_sensor',          '',             0x0001,     -1,  0,  0   ],
  'lowpressure_alm'              : ['r13', 'binary_sensor',          '',             0x0002,     -1,  0,  0   ],
  'motorbreaker_alm'             : ['r13', 'binary_sensor',          '',             0x0004,     -1,  0,  0   ],
  'brine_flow_alm'               : ['r13', 'binary_sensor',          '',             0x0008,     -1,  0,  0   ],
  'brine_temperature_alm'        : ['r13', 'binary_sensor',          '',             0x0010,     -1,  0,  0   ],
  'outdoor_sensor_alm'           : ['r14', 'binary_sensor',          '',             0x0001,     -1,  0,  0   ],
  'supplyline_sensor_alm'        : ['r14', 'binary_sensor',          '',             0x0002,     -1,  0,  0   ],
  'returnline_sensor_alm'        : ['r14', 'binary_sensor',          '',             0x0004,     -1,  0,  0   ],
  'boiler_sensor_alm'            : ['r14', 'binary_sensor',          '',             0x0008,     -1,  0,  0   ],
  'indoor_sensor_alm'            : ['r14', 'binary_sensor',          '',             0x0010,     -1,  0,  0   ],
  'phase_order_alm'              : ['r14', 'binary_sensor',          '',             0x0020,     -1,  0,  0   ],
  'overheating_alm'              : ['r14', 'binary_sensor',          '',             0x0040,     -1,  0,  0   ],
  'demand1'                      : ['r15', 'sensor',                 '',                  '',      '',  0,  0  ],
  'demand2'                      : ['r16', 'sensor',                 '',                  '',      '',  0,  0  ],
  'pressurepipe_t'               : ['r17', 'temperature',            'ºC',               '',      '',  0,  0  ],
  'hgw_water_t'                  : ['r18', 'temperature',            'ºC',               '',      '',  0,  0  ],
  'integral1'                    : ['r19', 'sensor',                 'Cmin',              '',      '',  2,  6  ],
  'integral1_a_step'             : ['r1a', 'sensor',                 '',                  '',      '',  0,  0  ],
  'defrost_time_m'               : ['r1b', 'time',                   '*10s',              '',      '',  0,  0  ],
  'time_to_start_min_m'          : ['r1c', 'time',                   'min',               '',      '',  0,  0  ],
  'sw_version'                   : ['r1d', 'sensor',                 '',                  '',      '',  0,  0  ],
  'supply_pump_speed'            : ['r1e', 'sensor',                 '%',                 '',      '',  2, 12  ],
  'brine_pump_speed'             : ['r1f', 'sensor',                 '%',                 '',      '',  2, 13  ],
  'status3_m'                    : ['r20', 'sensor',                 '',                  '',      '',  0,  0  ],
  'indoor_requested_t'           : ['r32', 'temperature_input',      'ºC',               0,     50,  4,  0  ],
  'main_mode'                    : ['r33', 'select_input',           '',                  0,     16,  1,  0  ],
  'integral1_curve_slope'        : ['r34', 'temperature_input',      'ºC',               0,    200,  4,  1  ],
  'integral1_curve_min'          : ['r35', 'temperature_input',      'ºC',               0,    200,  4,  2  ],
  'integral1_curve_max'          : ['r36', 'temperature_input',      'ºC',               0,    200,  4,  3  ],
  'integral1_curve_p5'           : ['r37', 'temperature_input',      'ºC',              -5,      5,  4,  4  ],
  'integral1_curve_0'            : ['r38', 'temperature_input',      'ºC',              -5,      5,  4,  5  ],
  'integral1_curve_n5'           : ['r39', 'temperature_input',      'ºC',              -5,      5,  4,  8  ],
  'heating_stop_t'               : ['r3a', 'temperature_input',      'ºC',               0,    200,  4,  8  ],
  'reduction_t'                  : ['r3b', 'temperature_input',      'ºC',               0,    100,  4, 10  ],
  'room_factor'                  : ['r3c', 'temperature_input',      'ºC',               0,      4,  4, 11  ],
  'integral2_curve_slope'        : ['r3d', 'temperature_input',      'ºC',               0,    200,  6,  0  ],
  'integral2_curve_min'          : ['r3e', 'temperature_input',      'ºC',               0,    200,  6,  1  ],
  'integral2_curve_max'          : ['r3f', 'temperature_input',      'ºC',               0,    200,  6,  2  ],
  'integral2_curve_target'       : ['r40', 'temperature_input',      'ºC',               0,    200,  6,  3  ],
  'integral2_curve_actual'       : ['r41', 'temperature_input',      'ºC',               0,    200,  6,  4  ],
  'outdoor_stop_t'               : ['r42', 'temperature_input',      'ºC',               0,    100,  7,  6  ],
  'pressure_pipe_limit_t'        : ['r43', 'temperature_input',      'ºC',               0,    200,  7,  5  ],
  'hotwater_start_t'             : ['r44', 'temperature_input',      'ºC',               0,    100,  5,  0  ],
  'hotwater_runtime_m'           : ['r45', 'time_input',             'min',               0,  32767,  5,  1  ],
  'heatpump_runtime_m'           : ['r46', 'time_input',             'min',               0,  32767,  5,  2  ],
  'legionella_interval_d'        : ['r47', 'time_input',             'days',              0,  32767,  5,  3  ],
  'legionella_stop_t'            : ['r48', 'temperature_input',      'ºC',               0,    100,  5,  4  ],
  'integral1_a_limit'            : ['r49', 'sensor_input',           'Cmin',         -32768,  32767,  7,  0  ],
  'integral1_hysteresis_t'       : ['r4a', 'temperature_input',      'ºC',               0,    100,  7,  1  ],
  'returnline_max_t'             : ['r4b', 'temperature_input',      'ºC',               0,    100,  7,  2  ],
  'start_interval_min_m'         : ['r4c', 'time_input',             'min',               0,  32767,  7,  3  ],
  'brine_min_t'                  : ['r4d', 'temperature_input',      'ºC',             -25,    100,  7,  4  ],
  'cooling_target_t'             : ['r4e', 'temperature_input',      'ºC',               0,     50,  7,  7  ],
  'integral2_a_limit'            : ['r4f', 'sensor_input',           '10 Cmin',           0,    200,  9,  0  ],
  'integral2_hysteresis_t'       : ['r50', 'temperature_input',      'ºC',               0,    100,  9,  1  ],
  'elect_boiler_steps_max'       : ['r51', 'sensor_input',           'steps',             0,      3,  9,  2  ],
  'current_consumption_max_a'    : ['r52', 'sensor_input',           'A',                 0,    100,  9,  3  ],
  'shunt_time_s'                 : ['r53', 'time_input',             's',                 0,  32767,  9,  4  ],
  'hotwater_stop_t'              : ['r54', 'temperature_input',      'ºC',               0,    100,  9,  5  ],
  'manual_test_mode_on'          : ['r55', 'sensor',                 '',                  '',      '', 10,  1  ],
  'status7'                      : ['r56', 'sensor',                 '',                  '',      '',  0,  0  ],
  'language'                     : ['r57', 'sensor_input',           '',                   0,     255, 10,  0  ],
  'status8'                      : ['r58', 'sensor',                 '',                  '',      '',  0,  0  ],
  'factory_reset_req'            : ['r59', 'sensor',                 'setting',           '',      '', 10,  2  ],
  'runtime_counters_reset_req'   : ['r5a', 'sensor',                 '',                  '',      '', 10,  3  ],
  'outdoor_sensor_offset_t'      : ['r5b', 'temperature_input',      'ºC',              -5,      5, 10,  4  ],
  'supplyline_sensor_offset_t'   : ['r5c', 'temperature_input',      'ºC',              -5,      5, 10,  5  ],
  'returnline_sensor_offset_t'   : ['r5d', 'temperature_input',      'ºC',              -5,      5, 10,  6  ],
  'boiler_sensor_offset_t'       : ['r5e', 'temperature_input',      'ºC',              -5,      5, 10,  7  ],
  'brine_in_sensor_offset_t'     : ['r5f', 'temperature_input',      'ºC',              -5,      5, 10,  8  ],
  'brine_out_sensor_offset_t'    : ['r60', 'temperature_input',      'ºC',              -5,      5, 10,  9  ],
  'heatingsystem_type'           : ['r61', 'sensor_input',           'type',         -32768,  32767, 10, 10  ],
  'opt_phasemeassure_installed'  : ['r62', 'binary_sensor',          '',             0x0001,     -1,  0,  0   ],
  'opt_2_installed'              : ['r62', 'binary_sensor',          '',             0x0002,     -1,  0,  0   ],
  'opt_hgw_installed'            : ['r62', 'binary_sensor',          '',             0x0004,     -1,  0,  0   ],
  'opt_4_installed'              : ['r62', 'binary_sensor',          '',             0x0008,     -1,  0,  0   ],
  'opt_5_installed'              : ['r62', 'binary_sensor',          '',             0x0010,     -1,  0,  0   ],
  'opt_6_installed'              : ['r62', 'binary_sensor',          '',             0x0020,     -1,  0,  0   ],
  'opt_optimum_installed'        : ['r62', 'binary_sensor',          '',             0x0040,     -1,  0,  0   ],
  'opt_flowguard_installed'      : ['r62', 'binary_sensor',          '',             0x0080,     -1,  0,  0   ],
  'internal_logging_t'           : ['r63', 'time_input',             'min',               0,  32767, 10, 11  ],
  'brine_runout_t'               : ['r64', 'time_input',             '*10s',              0,  32767, 10, 12  ],
  'brine_run_in_t'               : ['r65', 'time_input',             '*10s',              0,  32767, 10, 13  ],
  'legionella_run_on'            : ['r66', 'sensor_input',           '',                  0,      1, 10, 14  ],
  'legionella_run_length_h'      : ['r67', 'time_input',             'h',                 0,  32767, 10, 15  ],
  'compressor_runtime_h'         : ['r68', 'time',                   'h',                 '',      '',  3,  0  ],
  'msd1_dvp'                     : ['r69', 'sensor',                 '',                  '',      '',  0,  0  ],
  'boiler_3kw_runtime_h'         : ['r6a', 'time',                   'h',                 '',      '',  3,  1  ],
  'msd1_dts'                     : ['r6b', 'sensor',                 '',                  '',      '',  0,  0  ],
  'hotwater_runtime_h'           : ['r6c', 'time',                   'h',                 '',      '',  3,  3  ],
  'msd1_dvv'                     : ['r6d', 'sensor',                 '',                  '',      '',  0,  0  ],
  'passive_cooling_runtime_h'    : ['r6e', 'time',                   'h',                 '',      '',  3,  4  ],
  'msd1_dpas'                    : ['r6f', 'sensor',                 '',                  '',      '',  0,  0  ],
  'active_cooling_runtime_h'     : ['r70', 'time',                   'h',                 '',      '',  3,  5  ],
  'msd1_dact'                    : ['r71', 'sensor',                 '',                  '',      '',  0,  0  ],
  'boiler_6kw_on_runtime_h'      : ['r72', 'time',                   'h',                 '',      '',  3,  2  ],
  'msd1_dts2'                    : ['r73', 'sensor',                 '',                  '',      '',  0,  0  ],
  'graph_display_offset'         : ['r74', 'sensor',                 '',                  '',      '',  0,  0  ],
  'room_sensor_set_t'            : ['indr_t', 'generated_input',        'ºC',                0,     50, 0, 0 ],
  'time'                         : ['time', 'generated_sensor',       's',                 0,      0, 0, 0   ],
  'heatpump_evu_block'           : ['evu', 'generated_input',        '',                   0,      1, 0, 0   ],
  'mqtt_counter': ['mqtt_counter', 'generated_sensor', '', 0, 0, 0, 0],
    'time_str': ['time_str', 'generated_sensor', '', 0, 0, 0, 0],
    'rssi': ['rssi', 'generated_sensor', '', 0, 0, 0, 0],
    'communication_status': ['communication_status','generated_sensor','',0,0,0,0],

}

# Translation dictionary
id_names = {  
  'outdoor_t'                    : ['Outdoor temp.', 'Utomhustemp.', 'Ulkolämpötila', 'Utendørstemp.', 'Außentemperatur'],
  'indoor_t'                     : ['Indoor temp.', 'Rumstemp. är', 'Huonelämpötila', 'Romstemp. er', 'Innentemperatur, Ist'],
  'indoor_dec_t'                 : ['Indoor temp., decimal', 'Rumstemp. är, decimal', 'Huonelämpötila, desimaalit', 'Romstemp. er, desimal', 'Innentemp., Ist, decimal'],
  'indoor_target_t'              : ['Indoor target temp.', 'Rumstemp. bör', 'Haluttu huonelämpötila', 'Romstemp. bør', 'Innentemperatur, Soll'],
  'indoor_target_dec_t'          : ['Indoor target temp., decimal', 'Rumstemp. bör, decimal', 'Haluttu huonelämpötila, desimaalit', 'Romstemp. bør, desimal', 'Innentemp., Soll, decimal'],
  'supplyline_t'                 : ['Supplyline temp.', 'Framledningstemp.', 'Menovesi lämpötila', 'Turtemp.', 'Vorlauftemperatur'],
  'returnline_t'                 : ['Returnline temp.', 'Returledningstemp.', 'Paluuvesi lämpötila', 'Returtemp.', 'Rücklauftemperatur'],
  'boiler_t'                     : ['Hotwater temp.', 'Varmvattentemp.', 'Käyttöveden lämpötila', 'Varmtvannstemp.', 'Warmwassertemperatur'],
  'brine_out_t'                  : ['Brine out temp.', 'Brine ut temp.', 'Keruupiirin menolämpötila', 'Brine ut temp.', 'Soleablasstemperatur'],
  'brine_in_t'                   : ['Brine in temp.', 'Brine in temp.', 'Keruupiirin tulolämpötila', 'Brine inn temp.', 'Soleeinlasstemperatur'],
  'cooling_t'                    : ['Cooling temp.', 'Kylning temp.', 'Jäähdytys lämpötila', 'Kjølings temp.', 'Kühlung Temperatur'],
  'supply_shunt_t'               : ['Supplyline temp., shunt', 'Framledn.temp., shunt', 'Menovesi lämpötila, shuntti', 'Tur temp., shunt', 'Vorlauftemperatur, Mischer'],
  'current_consumed_a'           : ['Electrical Current', 'Strömförbrukning', 'Virran kulutus', 'Strømforbruk', 'Stromverbrauch'],
  'boiler_3kw_on'                : ['Aux. heater 3 kW', 'Tillsats 3 kW', 'Lisälämpö 3 kW', 'Tilskudd 3 kW', 'Elektrozusatz 3 kW'],
  'boiler_6kw_on'                : ['Aux. heater 6 kW', 'Tillsats 6 kW', 'Lisälämpö 6 kW', 'Tilskudd 6 kW', 'Elektrozusatz 6 kW'],
  'supplyline_target_t'          : ['Supplyline target temp.', 'Framledningstemp., bör', 'Haluttu menoveden lämpötila', 'Turtemp., bør', 'Vorlauftemperatur, Soll'],
  'supplyline_shunt_target_t'    : ['Supplyline target temp., shunt', 'Framledn.temp., shunt, bör', 'Haluttu menoveden lämpötila, shuntti', 'Tur temp., shunt, bør', 'Vorlauftemp., Mischer, Soll'],
  'brine_pump_on'                : ['Brinepump', 'Brinepump', 'Keruupumppu', 'Brinepumpe', 'Solepumpe'],
  'compressor_on'                : ['Compressor', 'Kompressor', 'Kompressori', 'Kompressor', 'Kompressor'],
  'supply_pump_on'               : ['Flowlinepump', 'Cirkulationspump', 'Kiertopumppu', 'Sirkulasjonspumpe', 'Umwälzpumpe'],
  'hotwaterproduction_on'        : ['Hotwater production.', 'Varmvattenprod.', 'Lämminvesituotanto', 'Varmtvannsprod.', 'Warmwasserbereitung'],
  'aux2_heating_on'              : ['Auxilliary 2', 'Tillsats 2', 'Lisälämpö 2', 'Tilskudd 2', 'Zusatzheizung 2'],
  'shunt1_n'                     : ['Shunt -', 'Shunt -', 'Shuntti -', 'Shunt -', 'Mischer -'],
  'shunt1_p'                     : ['Shunt +', 'Shunt +', 'Shuntti +', 'Shunt +', 'Mischer +'],
  'aux1_heating_on'              : ['Auxilliary 1', 'Tillsats 1', 'Lisälämpö 1', 'Tilskudd 1', 'Zusatzheizung 1'],
  'shunt2_n'                     : ['Shuntgroup -', 'Shuntgrupp -', 'Shunttiryhmä -', 'Shuntgruppe -', 'Mischergruppe -'],
  'shunt2_p'                     : ['Shuntgroup +', 'Shuntgrupp +', 'Shunttiryhmä +', 'Shuntgruppe +', 'Mischergruppe +'],
  'shunt_cooling_n'              : ['Shunt cooling -', 'Shunt kylning -', 'Shuntin jäähdytys -', 'Shunt kjøling -', 'Mischer Kühlung -'],
  'shunt_cooling_p'              : ['Shunt cooling +', 'Shunt kylning +', 'Shuntin jäähdytys +', 'Shunt kjøling +', 'Mischer Kühlung +'],
  'active_cooling_on'            : ['Active cooling', 'Aktiv kyla', 'Aktiivinen jäähdytys', 'Aktiv kjøling', 'Aktive Kühlung'],
  'passive_cooling_on'           : ['Passive cooling', 'Passiv kyla', 'Passiivinen jäähdytys', 'Passiv kjøling', 'Passive Külung'],
  'alarm_indication_on'          : ['Alarm', 'Larm', 'Hälytys', 'Alarm', 'Alarm'],
  'pwm_out_period'               : ['PWM Out', 'PWM Out', 'PWM Out', 'PWM Out', 'PWM Out'],
  'highpressure_alm'             : ['Alarm highpr.pressostate', 'Larm högtr.pressostat', 'Hälytys korkeapainesäädin', 'Alarmhøytr.pressostat', 'Alarm Hochdruckpressostat'],
  'lowpressure_alm'              : ['Alarm lowpr.pressostate', 'Larm lågtr.pressostat', 'Hälytys matalapainesäädin', 'Alarmlavtr.pressostat', 'Alarm Niedrigdruckpressostat'],
  'motorbreaker_alm'             : ['Alarm motorcircuit breaker', 'Larm motorskydd', 'Hälytys moottorisuoja', 'Alarmmotorvern', 'Alarm Motorschutz'],
  'brine_flow_alm'               : ['Alarm low flow brine', 'Larm lågflöde brine', 'Hälytys heikkovirtaus keruuliuos', 'Alarmlavflyt brine', 'Alarm Niedrigströmung, Sole'],
  'brine_temperature_alm'        : ['Alarm low temp. brine', 'Larm lågtemp. brine', 'Hälytys keruuliuoksen matala lämpötila', 'Alarmlavtemp. brine', 'Alarm Niedrigtemperatur, Sole'],
  'outdoor_sensor_alm'           : ['Alarm outdoor t-sensor', 'Larm utegivare', 'Hälytys ulkoanturi', 'Alarmutegiver', 'Alarm Außenfühler'],
  'supplyline_sensor_alm'        : ['Alarm supplyline t-sensor', 'Larm framledn.givare', 'Hälytys lämmityksen menoanturi', 'Alarmtur.giver', 'Alarm Vorlauffühler'],
  'returnline_sensor_alm'        : ['Alarm returnline t-sensor', 'Larm returledn.givare', 'Hälytys lämmityksen paluuanturi', 'Alarmretur.giver', 'Alarm Rücklauffühler'],
  'boiler_sensor_alm'            : ['Alarm hotw. t-sensor', 'Larm varmvattengivare', 'Hälytys lämminvesianturi', 'Alarmvarmtvannsgiver', 'Alarm Warmwasserfühler'],
  'indoor_sensor_alm'            : ['Alarm indoor t-sensor', 'Larm rumsgivare', 'Hälytys huoneanturi', 'Alarmromgiver', 'Alarm Innenfühler'],
  'phase_order_alm'              : ['Alarm incorrect 3-phase order', 'Larm fel fasföljd', 'Hälytys väärä vaihejärjestys', 'Alarmfeilfasefølge', 'Alarm falsche Phasenfolge'],
  'overheating_alm'              : ['Alarm overheating', 'Larm överhettningsskydd', 'Hälytys ylikuumenemissuoja', 'Alarmoveropphetningsvern', 'Alarm Überhitzungsschutz'],
  'demand1'                      : ['DEMAND1', 'BEHOV1', 'PYYNTÖ1', 'BEHOV1', 'BEDARF1'],
  'demand2'                      : ['DEMAND2', 'BEHOV2', 'PYYNTÖ2', 'BEHOV2', 'BEDARF2'],
  'pressurepipe_t'               : ['Pressurepipe temp.', 'Tryckrörtemp.', 'Paineputki lämpötila', 'Trykkrørstemp.', 'Druckrohrtemperatur'],
  'hgw_water_t'                  : ['Hotw. supplyline temp.', 'Varmv.framledn.temp', 'HGW menolämpötila', 'Varmtv.Tur temp', 'Warmw.vorlauftemperatur'],
  'integral1'                    : ['Integral (A1)', 'Integral (A1)', 'Integraali (A1)', 'Integral (A1)', 'Integral (A1)'],
  'integral1_a_step'             : ['Integral, reached A-limit', 'Integral, uppnådd A-gräns', 'Integraali, A-raja-arvo saavutettu', 'Integral, oppnådd A-grense', 'Integral, A-Grenzschritte'],
  'defrost_time_m'               : ['Defrost', 'Avfrostning', 'Sulatus', 'Defrost', 'Defrost'],
  'time_to_start_min_m'          : ['Minimum time to start', 'Minimum tid till start', 'Pienin aika käynnistymiseen', 'Minimum tid til start', 'Mindestzeit bis Start'],
  'sw_version'                   : ['Program version', 'Programversion', 'Ohjelmistoversio', 'Programversjon', 'Programmversion'],
  'supply_pump_speed'            : ['Flowlinepump speed', 'Cirk.pump fart', 'Kiertopumpun nopeus', 'Sirk.pump fart', 'Umwälzpumpengeschw.'],
  'brine_pump_speed'             : ['Brinepump speed', 'Brinepump fart', 'Keeruupumpun nopeus', 'Brinepumpe fart', 'Solepumpengeschw.'],
  'status3_m'                    : ['STATUS3', 'STATUS3', 'STATUS3', 'STATUS3', 'STATUS3'],
  'indoor_requested_t'           : ['Indoor target temp.', 'Rumstemp., bör', 'Haluttu huonelämpötila', 'Romstemp., bør', 'Innentemperatur, Soll'],
  'main_mode'                    : ['Mode', 'Driftläge', 'Käyttötila', 'Driftsmodus', 'Betriebszustand'],
  'integral1_curve_slope'        : ['Curve', 'Kurva', 'Käyrä', 'Kurve', 'Heizkurve'],
  'integral1_curve_min'          : ['Curve min', 'Kurva min', 'Käyrä min', 'Kurve min', 'Kurve min'],
  'integral1_curve_max'          : ['Curve max', 'Kurva max', 'Käyrä max', 'Kurve maks', 'Kurve max'],
  'integral1_curve_p5'           : ['Curve +5', 'Kurva +5', 'Käyrä +5', 'Kurve +5', 'Kurve +5'],
  'integral1_curve_0'            : ['Curve 0', 'Kurva 0', 'Käyrä 0', 'Kurve 0', 'Kurve 0'],
  'integral1_curve_n5'           : ['Curve -5', 'Kurva -5', 'Käyrä -5', 'Kurve -5', 'Kurve -5'],
  'heating_stop_t'               : ['Heatstop', 'Värmestopp', 'Lämmitys pois', 'Varmestopp', 'Heizstopp'],
  'reduction_t'                  : ['Temp. reduction', 'Temp. sänkning', 'Lämpötilan alennus', 'Temp. senkning', 'Nachtabsenkung'],
  'room_factor'                  : ['Room factor', 'Rumfaktor', 'Huonekerroin', 'Romfaktor', 'Raumfaktor'],
  'integral2_curve_slope'        : ['Curve 2', 'Shunt kurva', 'Shuntin käyrä', 'Shunt Kurve', 'Mischer Kurve'],
  'integral2_curve_min'          : ['Curve 2 min', 'Shunt kurva min', 'Shuntin käyrä, min', 'Shunt Kurve min', 'Mischer Kurve min'],
  'integral2_curve_max'          : ['Curve 2 max', 'Shunt kurva max', 'Shuntin käyrä, max', 'Shunt Kurve maks', 'Mischer Kurve max'],
  'integral2_curve_target'       : ['Curve 2, Target', 'Shunt kurva, bör', 'Shuntin käyrä, haluttu', 'Shunt Kurve, bør', 'Mischer Kurve, Soll'],
  'integral2_curve_actual'       : ['Curve 2, Actual', 'Shunt kurva, är', 'Shuntin käyrä, lämpötila', 'Shunt kurve, er', 'Mischer Kurve, Ist'],
  'outdoor_stop_t'               : ['Outdoor stop temp. (20=-20C)', 'Utestopp temp, (20=-20C)', 'Ulkolämpötila pysäytys (20=-20C)', 'Ute stop temp. (20=-20C)', 'Außentemp. Stop (20=-20C)'],
  'pressure_pipe_limit_t'        : ['Pressurepipe, temp. limit', 'Tryckrör, temp.gräns', 'Paineputki, lämpöraja', 'Trykkrør, temp.grense', 'Druckrohr, Temperaturgrenze'],
  'hotwater_start_t'             : ['Hotwater starttemp.', 'Varmvatten starttemp.', 'Lämminvesituotanto alkulämpötila', 'Varmtvann starttemp.', 'Warmwasser, Starttemperatur'],
  'hotwater_runtime_m'           : ['Hotwater operating time', 'Varmvattentid', 'Lämminvesi aika', 'Varmtvanntid', 'Warmwasserzeit'],
  'heatpump_runtime_m'           : ['Heatpump operating time', 'Värmetid', 'Lämmitysaika', 'Varmetid', 'Heizzeit'],
  'legionella_interval_d'        : ['Legionella interval', 'Legionella intervall', 'Legionella toiminnon väli', 'Legionella intervall', 'Legionella, Intervall'],
  'legionella_stop_t'            : ['Legionella stop temp.', 'Legionella stopptemp.', 'Legionellatoiminnon pysäytyslämpötila', 'Legionella stopptemp.', 'Legionella, Stopptemperatur'],
  'integral1_a_limit'            : ['Integral limit A1', 'Integralgräns A1', 'Integraaliraja A1', 'Integralgrense A1', 'Integral A1'],
  'integral1_hysteresis_t'       : ['Hysteresis A1', 'Hysteresgräns A1', 'Hystereesiraja lämpöpumppu A1', 'Hysteresegrense A1', 'Hysterese A1'],
  'returnline_max_t'             : ['Returnline temp., max limit', 'Returledningstemp., maxgräns', 'Paluuveden lämpötilan ylänraja', 'Returtemp., maksgrense', 'Rücklauftemperatur, Maxgrenze'],
  'start_interval_min_m'         : ['Minimum start interval', 'Minimum startintervall', 'Pienin käynnistysväli', 'Minimum startintervall', 'Minimum Startintervall'],
  'brine_min_t'                  : ['Brinetemp., min limit (-15=OFFV)', 'Brinetemp., min.gräns (-15=AV)', 'Keruulämpötilan alaraja (-15 pois päältä)', 'Brinetemp., min.grense (-15', 'Soletemperatur, Mingrenze (-15=aus)'],
  'cooling_target_t'             : ['Cooling, target', 'Kyla, bör', 'Jäähdytys haluttu lämpötila', 'Kjøling, bør', 'Kühlung, Soll'],
  'integral2_a_limit'            : ['Integral limit A2', 'Integralgräns A2', 'Integraaliraja A2', 'Integralgrense A2', 'Integral A2'],
  'integral2_hysteresis_t'       : ['Hysteresis limit A2', 'Hysteresgräns A2', 'Hystereesiraja lisälämpö', 'Hysteresegrense, Tilskudd', 'Hysterese, Zusatz'],
  'elect_boiler_steps_max'       : ['Max Electric steps', 'Max steg, tillsats', 'Max. lisälämmön portaat', 'Maks steg, Tilskudd', 'Maximum Stufen, Zusatz'],
  'current_consumption_max_a'    : ['Electrical current, max limit', 'Strömförbrukn., maxgräns', 'Virrankulutuksen yläraja', 'Strømforbrukn., maksgrense', 'Stromverbrauch, Maxgrenze'],
  'shunt_time_s'                 : ['Shunt time', 'Shunttid', 'Shunttiaika', 'Shunttid', 'Mischerzeit'],
  'hotwater_stop_t'              : ['Hotwater stop temp.', 'Varmvatten stopptemp.', 'Lämminvesi pysäytyslämpötila', 'Varmtvann stopptemp.', 'Warmwasserstopptemperatur'],
  'manual_test_mode_on'          : ['Manual test mode', 'Manuell test läge', 'Manuaalinen testaus', 'Manuell test modus', 'Manueller Test'],
  'status7'                      : ['DT_LARMOFF', 'DT_LARMOFF', 'DT_LARMOFF', 'DT_LARMOFF', 'DT_LARMOFF'],
  'language'                     : ['Language', 'Språk', 'Kieli', 'Språk', 'Sprache'],
  'status8'                      : ['SERVFAS', 'SERVFAS', 'SERVFAS', 'SERVFAS', 'SERVFAS'],
  'factory_reset_req'            : ['Reset to Factory settings', 'Fabriksinställningar', 'Palauta tehdasasetukset', 'Fabrikks instillinger', 'Werkseinstellung'],
  'runtime_counters_reset_req'   : ['Reset runtime counters', 'Nollställ drifttider', 'Nollaa käyntiajat', 'Nullstill drifttider', 'Nullstellung Laufzeiten'],
  'outdoor_sensor_offset_t'      : ['Calibration outdoor sensor', 'Kalibrering utegivare', 'Ulkoanturin kalibrointi', 'Kalibrering utegiver', 'Kalibrierung Außenfühler'],
  'supplyline_sensor_offset_t'   : ['Calibration supplyline sensor', 'Kalibrering framledn.givare', 'Menoanturin kalibrointi', 'Kalibrering tur.giver', 'Kalibrierung Vorlauffühler'],
  'returnline_sensor_offset_t'   : ['Calibration returnline sensor', 'Kalibrering returledn.givare', 'Paluuanturin kalibrointi', 'Kalibrering retur.giver', 'Kalibrierung Rücklauffühler'],
  'boiler_sensor_offset_t'       : ['Calibration hotwater sensor', 'Kalibrering varmvattengivare', 'Lämminvesianturin kalibrointi', 'Kalibrering Varmtvanngiver', 'Kalibrierung Warmwasserfühler'],
  'brine_in_sensor_offset_t'     : ['Calibration brine out sensor', 'Kalibrering brine ut', 'Keruu menoanturin kalibrointi', 'Kalibrering brine ut', 'Kalibrierung Soleablass'],
  'brine_out_sensor_offset_t'    : ['Calibration brine in sensor', 'Kalibrering brine in', 'Keruu paluuanturin kalibrointi', 'Kalibrering Brine inn', 'Kalibrierung Soleeinlass'],
  'heatingsystem_type'           : ['Heating system type 0=VL 4=D', 'Värmesystemtyp 0=VL 4=D', 'Lämmitysjärjestelmän tyyppi 0=VL 4=D', 'Varmesystemtype 0', 'Heizsystemtyp 0=VL 4=D'],
  'opt_phasemeassure_installed'  : ['Add-on phase order measurement', 'Tillägg fasmätning', 'Vaihejärjestysmittaus', 'Tillegg fasemåling', 'Ergänzung Phasenmessung'],
  'opt_2_installed'              : ['TILL2', 'TILL2', 'TILL2', 'TILL2', 'TILL2'],
  'opt_hgw_installed'            : ['Add-on HGW', 'Tillägg HGW', 'HGW lisätty', 'Tillegg HGW', 'Ergänzung HGW'],
  'opt_4_installed'              : ['TILL4', 'TILL4', 'TILL4', 'TILL4', 'TILL4'],
  'opt_5_installed'              : ['TILL5', 'TILL5', 'TILL5', 'TILL5', 'TILL5'],
  'opt_6_installed'              : ['TILL6', 'TILL6', 'TILL6', 'TILL6', 'TILL6'],
  'opt_optimum_installed'        : ['Add-on Optimum', 'Tillägg Optimum', 'Optimum lisätty', 'Tillegg Optimum', 'Ergänzung Optimum'],
  'opt_flowguard_installed'      : ['Add-on flow guard', 'Tillägg flödesvakt', 'Virtausvahti lisätty', 'Tillegg flytvakt', 'Ergänzung Strömungswächter'],
  'internal_logging_t'           : ['Logging time', 'Loggtid', 'Lokiaika', 'Loggtid', 'Logdauer'],
  'brine_runout_t'               : ['Brine run-out duration', 'Brinetid på', 'Keruupumpun käyntiaika', 'Brinetid på', 'Solepumpe Anlaufdauer'],
  'brine_run_in_t'               : ['Brine run-in duration', 'Brinetid av', 'Keruupumpun pysähdysaika', 'Brinetid av', 'Solepumpe Nachlaufdauer'],
  'legionella_run_on'            : ['Legionella peak heating enable', 'Tillåt legionella körning', 'Legionella  toiminnon käynnistys', 'Legionella topptid aktiv', 'Legionella Spitzenwärme aktiv'],
  'legionella_run_length_h'      : ['Legionella peak heating duration', 'Legionella topptid', 'Legionella toiminnon huippulämmön aika', 'Legionella topptid', 'Legionella Spitzenwärmedauer'],
  'compressor_runtime_h'         : ['Runtime compressor', 'Drifttid kompressor', 'Kompressorin käyntiaika', 'Drifttid kompressor', 'Betriebszeit Kompressor'],
  'msd1_dvp'                     : ['DVP_MSD1', 'DVP_MSD1', 'DVP_MSD1', 'DVP_MSD1', 'DVP_MSD1'],
  'boiler_3kw_runtime_h'         : ['Runtime 3 kW', 'Drifttid 3 kW', 'Käyttöaika 3 kW', 'Drifttid 3 kW', 'Betriebszeit 3 kW'],
  'msd1_dts'                     : ['DTS_MSD1', 'DTS_MSD1', 'DTS_MSD1', 'DTS_MSD1', 'DTS_MSD1'],
  'hotwater_runtime_h'           : ['Runtime hotwater production', 'Drifttid varmv.prod. med kompr.', 'Käyttöaika lämminvesi (kompressorilla)', 'Drifttid Varmtv.prod. med kompr.', 'Betriebszeit Warmwasser'],
  'msd1_dvv'                     : ['DVV_MSD1', 'DVV_MSD1', 'DVV_MSD1', 'DVV_MSD1', 'DVV_MSD1'],
  'passive_cooling_runtime_h'    : ['Runtime passive cooling', 'Drifttid passiv kyla', 'Käyttöaika passiviseen viilennykseen', 'Drifttid passiv kjøling', 'Betriebszeit passive Kühlung'],
  'msd1_dpas'                    : ['DPAS_MSD1', 'DPAS_MSD1', 'DPAS_MSD1', 'DPAS_MSD1', 'DPAS_MSD1'],
  'active_cooling_runtime_h'     : ['Runtime active cooling', 'Drifttid aktiv kyla', 'Käyttöaika aktiviseen viilennykseen', 'Drifttid aktiv kjøling', 'Betriebszeit aktive Kühlung'],
  'msd1_dact'                    : ['DACT_MSD1', 'DACT_MSD1', 'DACT_MSD1', 'DACT_MSD1', 'DACT_MSD1'],
  'boiler_6kw_on_runtime_h'      : ['Runtime 6 kW', 'Drifttid 6 kW', 'Käyttöaika 6 kW', 'Drifttid 6 kW', 'Betriebszeit 6 kW'],
  'msd1_dts2'                    : ['DTS2_MSD1', 'DTS2_MSD1', 'DTS2_MSD1', 'DTS2_MSD1', 'DTS2_MSD1'],
  'graph_display_offset'         : ['GrafCounterOffSet', 'GrafCounterOffSet', 'GrafCounterOffSet', 'GrafCounterOffSet', 'GrafCounterOffSet'],
  'room_sensor_set_t'            : ['Room sensor, Set actual','Rums sensor, Sätt nuvarande', 'Huoneanturin tavoitelämpötila', 'Room sensor, Set', 'Room sensor, Set'],
  'heatpump_evu_block'           : ['EVU Function, Set state','EVU funktion, Läge','EVU toiminnon tila','EVU Function, Set state','EVU Function, Set state' ]n  "mode0": ["Off", "Av", "Pois päältä", "Off", "Aus"],
    "mode1": ["Auto", "Auto", "Auto", "Auto", "Auto"],
    "mode2": ["Heatpump only", "Bara värmepump", "Vain lämpöpumppu", "Kun varmepumpe", "Nur Wärmepumpe"],
    "mode4": ["Heater only", "Elvärme", "Vain lisälämpö", "Kun elektrisk oppvarming", "Nur Elektroheizung"],
    "mode8": ["Hot water only", "Bara varmvatten", "Vain käyttövesituotanto", "Kun varmtvannsbereder", "Nur Warmwasserbereiter"],
}