def export_dataset_ris_format(request, dataset_version_id):
    """
    Export dataset in ris format
    """
    dataset_biz = DatasetBiz.biz()

    export_file = dataset_biz.export_dataset_ris_format(dataset_version_id)

    return export_file