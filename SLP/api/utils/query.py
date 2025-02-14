class DBHandler:
    @classmethod
    def query_content_type(cls, mls_num):
        return f''' select ctm.content_sub_type, ctm.resource_name
    from download_mls dm
    left join mls m ON m.id = dm.mls_id
    left join download_config dc on dc.id  = dm.download_config_id
    left join mls_resource mr on mr.mls_id = dm.mls_id
    left join process_map pm on pm.id = mr.process_map_id
    left join content_type_map ctm on ctm.id = mr.content_type_map_id
    left join download_protocol dp on dp.id = dc.download_protocol_id
    where m.id = {mls_num}
    and m.is_parent_mls = true
    and pm.properties is not null'''

    @classmethod
    def query_map(cls, mls_num, content_type, resource_name):
        return f''' select pm.properties
            from download_mls dm 
            left join mls m ON m.id = dm.mls_id 
            left join download_config dc on dc.id  = dm.download_config_id 
            left join mls_resource mr on mr.mls_id = dm.mls_id  
            left join process_map pm on pm.id = mr.process_map_id 
            left join content_type_map ctm on ctm.id = mr.content_type_map_id 
            left join download_protocol dp on dp.id = dc.download_protocol_id 
                where ctm.content_sub_type = '{content_type}'
                and ctm.resource_name = '{resource_name}'
            and m.id = {mls_num}
            and m.is_parent_mls = true
            and pm.properties is not null'''

    @classmethod
    def query_download(cls, mls_num):
        return f''' 	select qt.name, qt.template 
            from download_mls dm
            left outer join download_config dc on dc.id = dm.download_config_id
            left outer join download_mls_query dmq on dmq.download_mls_id = dm.id
            left outer join download_type dt on dt.id = dmq.download_type_id
            left outer join content_type_map ctm on ctm.id = dmq.content_type_map_id
            left outer join query_template qt on qt.id = dmq.query_template_id
            where dm.mls_id = {mls_num};'''

    @classmethod
    def config_downloads_names(cls, mls_num):
        return f''' 	select qt.name 
                        from download_mls dm
                        left outer join download_config dc on dc.id = dm.download_config_id
                        left outer join download_mls_query dmq on dmq.download_mls_id = dm.id
                        left outer join download_type dt on dt.id = dmq.download_type_id
                        left outer join content_type_map ctm on ctm.id = dmq.content_type_map_id
                        left outer join query_template qt on qt.id = dmq.query_template_id
                        where dm.mls_id = {mls_num};'''

    @classmethod
    def config_downloads_queries(cls, mls_num, query_name):
        return f''' 	select qt.name, dc.config, dc.secrets, dmq.query_params, qt.template, dmq.custom_config 
    from download_mls dm
    left outer join download_config dc on dc.id = dm.download_config_id
    left outer join download_mls_query dmq on dmq.download_mls_id = dm.id
    left outer join download_type dt on dt.id = dmq.download_type_id
    left outer join content_type_map ctm on ctm.id = dmq.content_type_map_id
    left outer join query_template qt on qt.id = dmq.query_template_id
    where dm.mls_id = {mls_num}
    and qt.name = '{query_name}';'''
