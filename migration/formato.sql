
,isnull(case when instr(f021_descripcion,'-') < 2 then f021_descripcion else substring(f021_descripcion,1,instr(f021_descripcion,'-')-1) end,' ') f_desc_tp_docto  
,isnull(rtrim(f022_nro_resolucion),' ') f_res_fact  
,isnull(to_char(f022_fecha_resolucion,'YYY/MM/DD'),' ') f_fecha_res_fact  
,isnull(to_char(f022_fecha_resolucion_vcto,'YYY/MM/DD'),' ') f_fecha_vcto_res_fact  
,isnull(rtrim(f022_prefijo),' ')+cast(f022_cons_inicial as varchar(20)) f_cons_ini_res_fact  
,isnull(rtrim(f022_prefijo),' ')+cast(f022_cons_final as varchar(20)) f_cons_fin_res_fact  
,isnull(rtrim(f022_prefijo),' ') f_prefijo_res_fact  
,cast(round(months_between(f022_fecha_resolucion_vcto,f022_fecha_resolucion),0) as varchar(20))+case when months_between(f022_fecha_resolucion_vcto,f022_fecha_resolucion) = 1 then ' Mes' else ' Meses' end f_vigencia_res_fact  
,left(dbo.f_generico_hallar_movto_ent(f461_id_cia,f021_rowid_movto_entidad,'EUNOECO007','co007_notaEnc1',1),255) f_ent_nota_enc_res_fact  
,f_resol_fact_autoriza_habilita(f350_rowid) f_halilita_autoriza_res_fact  
,isnull(rtrim(t_id_tp_cli.f_desc_tipo_id_cli),'') f_tipo_id_cliente  
,left(to_char(f350_fecha_ts_aprobacion,'HH:MI:SS'),7) f_fecha_aprobacion_fact  
,left(dbo.f_generico_hallar_movto_ent(@cia,f208_rowid_movto_entidad,'EUNOECO021','co021_forma_pago',1),40) f_forma_pago  
,left(dbo.f_generico_hallar_movto_ent(@cia,f025_rowid_movto_entidad,'EUNOECO018','co018_medio_pago',1) + '-' + dbo.f_generico_hallar_movto_ent(@cia,f025_rowid_movto_entidad,'EUNOECO018','co018_medio_pago',8),40) f_medio_pago  
,'Factura Generada por Software Sistemas de Informacion Empresarial S.A. Nit: 890.319.193-3' f_txt_impresor  
