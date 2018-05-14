from rest_framework.utils import json
from coinmarketcap import Market
import time
import psycopg2


def main():
    """
        Valid FIAT and CRYPTO Currency values for convert parameter:
    """

    currency = [
        "aud", "brl", "cad", "chf", "clp", "cny", "czk", "dkk", "eur", "gbp",
        "hkd", "huf", "idr", "ils", "inr", "jpy", "krw", "mxn", "myr", "nok",
        "nzd", "php", "pkr", "pln", "rub", "sek", "sgd", "thb", "try", "twd",
        "zar", "btc", "eth", "xrp", "ltc", "bch"]

    """
        DROP TABLE <table1, table2, etc> CASCADE;
        DROP TABLE aud, brl, cad, chf, clp, cny, czk, dkk, eur, gbp, hkd, huf, idr, ils, inr, jpy, krw, mxn CASCADE;
        DROP TABLE myr, nok, nzd, php, pkr, pln, rub, sek, sgd, thb, try, twd, zar, btc, eth, xrp, ltc, bch CASCADE;
    """

    main_fields = [
        'name_id',
        'name',
        'symbol',
        'rank',
        'prices_usd',
        'prices_btc',
        'volume_usd_24h',
        'market_usd_cap',
        'available_supply',
        'total_supply',
        'max_supply',
        'percent_change_1h',
        'percent_change_24h',
        'percent_change_7d',
        'last_updated',
        'cached'
    ]

    currency_fields = [
        'prices_btc', 'volume_btc_24h', 'market_btc_cap',
        'prices_eth', 'volume_eth_24h', 'market_eth_cap',
        'prices_xrp', 'volume_xrp_24h', 'market_xrp_cap',
        'prices_ltc', 'volume_ltc_24h', 'market_ltc_cap',
        'prices_bch', 'volume_bch_24h', 'market_bch_cap',
        'prices_eur', 'volume_eur_24h', 'market_eur_cap',
        'prices_aud', 'volume_aud_24h', 'market_aud_cap',
        'prices_brl', 'volume_brl_24h', 'market_brl_cap',
        'prices_cad', 'volume_cad_24h', 'market_cad_cap',
        'prices_chf', 'volume_chf_24h', 'market_chf_cap',
        'prices_clp', 'volume_clp_24h', 'market_clp_cap',
        'prices_cny', 'volume_cny_24h', 'market_cny_cap',
        'prices_czk', 'volume_czk_24h', 'market_czk_cap',
        'prices_dkk', 'volume_dkk_24h', 'market_dkk_cap',
        'prices_gbp', 'volume_gbp_24h', 'market_gbp_cap',
        'prices_hkd', 'volume_hkd_24h', 'market_hkd_cap',
        'prices_huf', 'volume_huf_24h', 'market_huf_cap',
        'prices_idr', 'volume_idr_24h', 'market_idr_cap',
        'prices_ils', 'volume_ils_24h', 'market_ils_cap',
        'prices_inr', 'volume_inr_24h', 'market_inr_cap',
        'prices_jpy', 'volume_jpy_24h', 'market_jpy_cap',
        'prices_krw', 'volume_krw_24h', 'market_krw_cap',
        'prices_mxn', 'volume_mxn_24h', 'market_mxn_cap',
        'prices_myr', 'volume_myr_24h', 'market_myr_cap',
        'prices_nok', 'volume_nok_24h', 'market_nok_cap',
        'prices_nzd', 'volume_nzd_24h', 'market_nzd_cap',
        'prices_php', 'volume_php_24h', 'market_php_cap',
        'prices_pkr', 'volume_pkr_24h', 'market_pkr_cap',
        'prices_pln', 'volume_pln_24h', 'market_pln_cap',
        'prices_rub', 'volume_rub_24h', 'market_rub_cap',
        'prices_sek', 'volume_sek_24h', 'market_sek_cap',
        'prices_sgd', 'volume_sgd_24h', 'market_sgd_cap',
        'prices_thb', 'volume_thb_24h', 'market_thb_cap',
        'prices_try', 'volume_try_24h', 'market_try_cap',
        'prices_twd', 'volume_twd_24h', 'market_twd_cap',
        'prices_zar', 'volume_zar_24h', 'market_zar_cap'
    ]

    conn = psycopg2.connect(host='127.0.0.1', dbname='cryptos', user='crypto', password='0lympu$24$jmfISU')
    cur = conn.cursor()

    ingest = Ingest(currency, conn, cur, main_fields, currency_fields)
    start = time.time()

    print("*** Create Tables ***")
    ingest.create_tables(conn, cur)

    while True:
        print("*** Group One ***")
        ingest.group_one(conn, cur, main_fields, currency_fields)
        time.sleep(60.0 - ((time.time() - start) % 60.0))

        print('*** Group Two ***')
        ingest.group_two(conn, cur, main_fields, currency_fields)
        time.sleep(60.0 - ((time.time() - start) % 60.0))

        print('***Group Three***')
        ingest.group_three(conn, cur, main_fields, currency_fields)
        time.sleep(60.0 - ((time.time() - start) % 60.0))

        print('***Group Four***')
        ingest.group_four(conn, cur, main_fields, currency_fields)
        time.sleep(120.0 - ((time.time() - start) % 120.0))


class Ingest(object):

    def __init__(self, currency, conn, cur, main_fields, currency_fields):
        self.data = currency
        self.conn = conn
        self.cur = cur
        self.main_fields = main_fields
        self.currency_fields = currency_fields

    @staticmethod
    def create_tables(conn, cur):

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS main (
                id INTEGER PRIMARY KEY, 
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time
                )
            """
        )
        conn.commit()

        tables = [(
            """
                CREATE TABLE IF NOT EXISTS btc(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_btc float, volume_btc_24h float, market_btc_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS eth(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_eth float, volume_eth_24h float, market_eth_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS xrp(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_xrp float, volume_xrp_24h float, market_xrp_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS ltc(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_ltc float, volume_ltc_24h float, market_ltc_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS bch(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_bch float, volume_bch_24h float, market_bch_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS aud(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_aud float, volume_aud_24h float, market_aud_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS brl(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_brl float, volume_brl_24h float, market_brl_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS cad(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_cad float, volume_cad_24h float, market_cad_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS chf(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_chf float, volume_chf_24h float, market_chf_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS clp(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_clp float, volume_clp_24h float, market_clp_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS cny(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_cny float, volume_cny_24h float, market_cny_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS czk(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_czk float, volume_czk_24h float, market_czk_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS dkk(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_dkk float, volume_dkk_24h float, market_dkk_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS eur(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_eur float, volume_eur_24h float, market_eur_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS gbp(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_gbp float, volume_gbp_24h float, market_gbp_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS hkd(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_hkd float, volume_hkd_24h float, market_hkd_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS huf(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_huf float, volume_huf_24h float, market_huf_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS idr(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_idr float, volume_idr_24h float, market_idr_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS ils(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_ils float, volume_ils_24h float, market_ils_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS inr(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_inr float, volume_inr_24h float, market_inr_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS jpy(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_jpy float, volume_jpy_24h float, market_jpy_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS krw(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_krw float, volume_krw_24h float, market_krw_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS mxn(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_mxn float, volume_mxn_24h float, market_mxn_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS myr(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_myr float, volume_myr_24h float, market_myr_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS nok(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_nok float, volume_nok_24h float, market_nok_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS nzd(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_nzd float, volume_nzd_24h float, market_nzd_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS php(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_php float, volume_php_24h float, market_php_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS pkr(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_pkr float, volume_pkr_24h float, market_pkr_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS pln(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_pln float, volume_pln_24h float, market_pln_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS rub(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_rub float, volume_rub_24h float, market_rub_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS sek(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_sek float, volume_sek_24h float, market_sek_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS sgd(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_sgd float, volume_sgd_24h float, market_sgd_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS thb(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_thb float, volume_thb_24h float, market_thb_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS try(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_try float, volume_try_24h float, market_try_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS twd(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_twd float, volume_twd_24h float, market_twd_cap float)
            """), (
            """
                CREATE TABLE IF NOT EXISTS zar(
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd float,
                prices_btc float, 
                volume_usd_24h float, 
                market_usd_cap float,
                available_supply float, 
                total_supply float, 
                max_supply float,
                percent_change_1h float, 
                percent_change_24h float, 
                percent_change_7d float,
                last_updated float, 
                cached varchar, 
                created_at time, 
                updated_at time,
                prices_zar float, volume_zar_24h float, market_zar_cap float)
            """
        )]

        for table in tables:
            cur.execute(table)
            conn.commit()

    def group_one(self, conn, cur, main_fields, currency_fields):

        group_one = self.data[0:10]

        for currencies in group_one:
            crypto = json.dumps(Market().ticker(start=0, limit=0, convert=currencies))
            crypto = json.loads(crypto)

            for cryptos in crypto:
                data = {
                    'name_id': cryptos['id'],
                    'name': cryptos['name'],
                    'symbol': cryptos['symbol'],
                    'rank': cryptos['rank'],
                    'prices_usd': cryptos['price_usd'],
                    'prices_btc': cryptos['price_btc'],
                    'volume_usd_24h': cryptos['24h_volume_usd'],
                    'market_usd_cap': cryptos['market_cap_usd'],
                    'available_supply': cryptos['available_supply'],
                    'total_supply': cryptos['total_supply'],
                    'max_supply': cryptos['max_supply'],
                    'percent_change_1h': cryptos['percent_change_1h'],
                    'percent_change_24h': cryptos['percent_change_24h'],
                    'percent_change_7d': cryptos['percent_change_7d'],
                    'last_updated': cryptos['last_updated'],
                    'cached': cryptos['cached'],
                    'prices_' + currencies: cryptos['price_' + currencies],
                    'volume_' + currencies + '_24h': cryptos['24h_volume_' + currencies],
                    'market_' + currencies + '_cap': cryptos['market_cap_' + currencies]
                }

                for currency in currency_fields:
                    if currencies == currency[7:10]:
                        main_fields.append(currency)

                cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")

                for table in cur.fetchall():
                    if table[0] == currencies:
                        for column in tuple(data):
                            cur.execute("INSERT INTO " + table[0] + " (" + column + ") VALUES (%s)", (data[column],))
                            # cur.execute("UPDATE " + table[0] + " SET " + column + "=(%s)", (data[column],))
        conn.commit()
        print("*** COMMIT GROUP ONE ***")

    def group_two(self, conn, cur, main_fields, currency_fields):

        group_two = self.data[10:20]

        for currencies in group_two:
            crypto = json.dumps(Market().ticker(start=0, limit=0, convert=currencies))
            crypto = json.loads(crypto)

            for cryptos in crypto:
                data = {
                    'name_id': cryptos['id'],
                    'name': cryptos['name'],
                    'symbol': cryptos['symbol'],
                    'rank': cryptos['rank'],
                    'prices_usd': cryptos['price_usd'],
                    'prices_btc': cryptos['price_btc'],
                    'volume_usd_24h': cryptos['24h_volume_usd'],
                    'market_usd_cap': cryptos['market_cap_usd'],
                    'available_supply': cryptos['available_supply'],
                    'total_supply': cryptos['total_supply'],
                    'max_supply': cryptos['max_supply'],
                    'percent_change_1h': cryptos['percent_change_1h'],
                    'percent_change_24h': cryptos['percent_change_24h'],
                    'percent_change_7d': cryptos['percent_change_7d'],
                    'last_updated': cryptos['last_updated'],
                    'cached': cryptos['cached'],
                    'prices_' + currencies: cryptos['price_' + currencies],
                    'volume_' + currencies + '_24h': cryptos['24h_volume_' + currencies],
                    'market_' + currencies + '_cap': cryptos['market_cap_' + currencies]
                }

                for currency in currency_fields:
                    if currencies == currency[7:10]:
                        main_fields.append(currency)

                cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")

                for table in cur.fetchall():
                    if table[0] == currencies:
                        for column in tuple(data):
                            cur.execute("INSERT INTO " + table[0] + " (" + column + ") VALUES (%s)", (data[column],))
                            # cur.execute("UPDATE " + table[0] + " SET " + column + "=(%s)", (data[column],))
        conn.commit()
        print("*** COMMIT GROUP TWO ***")

    def group_three(self, conn, cur, main_fields, currency_fields):

        group_three = self.data[20:30]

        for currencies in group_three:
            crypto = json.dumps(Market().ticker(start=0, limit=0, convert=currencies))
            crypto = json.loads(crypto)

            for cryptos in crypto:
                data = {
                    'name_id': cryptos['id'],
                    'name': cryptos['name'],
                    'symbol': cryptos['symbol'],
                    'rank': cryptos['rank'],
                    'prices_usd': cryptos['price_usd'],
                    'prices_btc': cryptos['price_btc'],
                    'volume_usd_24h': cryptos['24h_volume_usd'],
                    'market_usd_cap': cryptos['market_cap_usd'],
                    'available_supply': cryptos['available_supply'],
                    'total_supply': cryptos['total_supply'],
                    'max_supply': cryptos['max_supply'],
                    'percent_change_1h': cryptos['percent_change_1h'],
                    'percent_change_24h': cryptos['percent_change_24h'],
                    'percent_change_7d': cryptos['percent_change_7d'],
                    'last_updated': cryptos['last_updated'],
                    'cached': cryptos['cached'],
                    'prices_' + currencies: cryptos['price_' + currencies],
                    'volume_' + currencies + '_24h': cryptos['24h_volume_' + currencies],
                    'market_' + currencies + '_cap': cryptos['market_cap_' + currencies]
                }

                for currency in currency_fields:
                    if currencies == currency[7:10]:
                        main_fields.append(currency)

                cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")

                for table in cur.fetchall():
                    if table[0] == currencies:
                        for column in tuple(data):
                            cur.execute("INSERT INTO " + table[0] + " (" + column + ") VALUES (%s)", (data[column],))
                            # cur.execute("UPDATE " + table[0] + " SET " + column + "=(%s)", (data[column],))
        conn.commit()
        print("*** COMMIT GROUP THREE***")

    def group_four(self, conn, cur, main_fields, currency_fields):

        group_four = self.data[30:]

        for currencies in group_four:
            crypto = json.dumps(Market().ticker(start=0, limit=0, convert=currencies))
            crypto = json.loads(crypto)

            for cryptos in crypto:
                data = {
                    'name_id': cryptos['id'],
                    'name': cryptos['name'],
                    'symbol': cryptos['symbol'],
                    'rank': cryptos['rank'],
                    'prices_usd': cryptos['price_usd'],
                    'prices_btc': cryptos['price_btc'],
                    'volume_usd_24h': cryptos['24h_volume_usd'],
                    'market_usd_cap': cryptos['market_cap_usd'],
                    'available_supply': cryptos['available_supply'],
                    'total_supply': cryptos['total_supply'],
                    'max_supply': cryptos['max_supply'],
                    'percent_change_1h': cryptos['percent_change_1h'],
                    'percent_change_24h': cryptos['percent_change_24h'],
                    'percent_change_7d': cryptos['percent_change_7d'],
                    'last_updated': cryptos['last_updated'],
                    'cached': cryptos['cached'],
                    'prices_' + currencies: cryptos['price_' + currencies],
                    'volume_' + currencies + '_24h': cryptos['24h_volume_' + currencies],
                    'market_' + currencies + '_cap': cryptos['market_cap_' + currencies]
                }

                for currency in currency_fields:
                    if currencies == currency[7:10]:
                        main_fields.append(currency)

                cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")

                for table in cur.fetchall():
                    if table[0] == currencies:
                        for column in tuple(data):
                            cur.execute("INSERT INTO " + table[0] + " (" + column + ") VALUES (%s)", (data[column],))
                            # cur.execute("UPDATE " + table[0] + " SET " + column + "=(%s)", (data[column],))
        conn.commit()
        print("*** COMMIT GROUP FOUR ***")


if __name__ == '__main__':
    main()
