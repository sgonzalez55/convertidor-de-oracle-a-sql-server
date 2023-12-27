import re
import sqlite3


def convertir_plsql_a_sql(codigo_plsql):
    
    reglas_conversion = [
        (r'DECLARE(.*?)BEGIN', r''),
        (r'END;', r''),
        (r':=', r'='),
        (r'v_', r'@_'),
        (r'varchar2', r'varchar'),
        (r'VARCHAR2', r'varchar'),
        (r'DATE',r'datetime'),
        (r'nvl',r'isnull'),
        (r'NVL',r'isnull'),
        (r'NUMBER\s*\(\s*\d+\s*,\s*[1-9]\d*\s*\)', r'money'),  #NUMBER(25,4)
        (r'NUMBER\s*\(\s*\d+\s*,\s*0\s*\)\s*[,;]*', r'smallint'),#NUMBER(5,0)
        (r'\|\|', r'+'),
        (r'create global temporary table fmt_tp1',r'create table #tp1_pv_cons_fact'),
        (r'create global temporary table fmt_tp2',r'create table #tp2_pv_cons_fact'),
        (r';',r''),
        (r'F_GENERICO_HALLAR_MOVTO_ENT',r'dbo.F_GENERICO_HALLAR_MOVTO_ENT'),
        (r'f_generico_hallar_movto_ent',r'dbo.f_generico_hallar_movto_ent'),
        (r'p_cia',r'@cia')
        
    ]


    for patron, reemplazo in reglas_conversion:
        codigo_plsql = re.sub(patron, reemplazo, codigo_plsql, flags=re.DOTALL)


    return codigo_plsql


codigo_plsql = """
,nvl(case when instr(f021_descripcion,'-') < 2 then f021_descripcion else substring(f021_descripcion,1,instr(f021_descripcion,'-')-1) end,' ') f_desc_tp_docto  
,nvl(rtrim(f022_nro_resolucion),' ') f_res_fact  
,nvl(to_char(f022_fecha_resolucion,'YYY/MM/DD'),' ') f_fecha_res_fact  
,nvl(to_char(f022_fecha_resolucion_vcto,'YYY/MM/DD'),' ') f_fecha_vcto_res_fact  
,nvl(rtrim(f022_prefijo),' ')||cast(f022_cons_inicial as varchar2(20)) f_cons_ini_res_fact  
,nvl(rtrim(f022_prefijo),' ')||cast(f022_cons_final as varchar2(20)) f_cons_fin_res_fact  
,nvl(rtrim(f022_prefijo),' ') f_prefijo_res_fact  
,cast(round(months_between(f022_fecha_resolucion_vcto,f022_fecha_resolucion),0) as varchar2(20))||case when months_between(f022_fecha_resolucion_vcto,f022_fecha_resolucion) = 1 then ' Mes' else ' Meses' end f_vigencia_res_fact  
,left(f_generico_hallar_movto_ent(f461_id_cia,f021_rowid_movto_entidad,'EUNOECO007','co007_notaEnc1',1),255) f_ent_nota_enc_res_fact  
,f_resol_fact_autoriza_habilita(f350_rowid) f_halilita_autoriza_res_fact  
,nvl(rtrim(t_id_tp_cli.f_desc_tipo_id_cli),'') f_tipo_id_cliente  
,left(to_char(f350_fecha_ts_aprobacion,'HH:MI:SS'),7) f_fecha_aprobacion_fact  
,left(f_generico_hallar_movto_ent(p_cia,f208_rowid_movto_entidad,'EUNOECO021','co021_forma_pago',1),40) f_forma_pago  
,left(f_generico_hallar_movto_ent(p_cia,f025_rowid_movto_entidad,'EUNOECO018','co018_medio_pago',1) || '-' || f_generico_hallar_movto_ent(p_cia,f025_rowid_movto_entidad,'EUNOECO018','co018_medio_pago',8),40) f_medio_pago  
,'Factura Generada por Software Sistemas de Informacion Empresarial S.A. Nit: 890.319.193-3' f_txt_impresor  
"""

codigo_sql = convertir_plsql_a_sql(codigo_plsql)
resultado_query = codigo_sql
nombre_archivo = "formato.sql"

with open(nombre_archivo, 'w') as archivo_sql:
    archivo_sql.write(resultado_query)
print(codigo_sql)
print("***Guardado***")
