    def export_dataset_ris_format(self, dataset_version_id):
        dataset_version = get_object(DatasetVersion, pk=dataset_version_id)
        dataset = get_object(Dataset, pk=dataset_version.dataset_id)
        study_dataset_information = get_object(StudyDatasetInformation, pk=dataset.study_dataset_information_id)
        study = get_object(Study, pk=study_dataset_information.study_id)
        latest_study_version_published = get_object_or_none(StudyVersion, pk=study.latest_published_version_id)
        study_version_translation = StudyVersionTranslation.objects.filter(study_version_id=latest_study_version_published.id, language_id=latest_study_version_published.language_id)
        study_version_persons = StudyPerson.objects.filter(study_version_id=latest_study_version_published.id)

        investigator = []
        for study_version_person in study_version_persons:
            if study_version_person.person_id:
                investigator.append(study_version_person.person.lastname + "," + study_version_person.person.firstname)
            else:
                investigator.append(study_version_person.last_name + "," + study_version_person.first_name)

        dataset_language_translation = get_object(LanguageTranslation, language_id=dataset_version.language, language_translation_id=dataset_version.language)
        dataset_translation = DatasetTranslation.objects.filter(dataset_id=dataset_version.dataset_id, language_id=dataset_version.language_id)
        dataset_title = str(dataset_translation[0].title.replace("\r\n", " ")) + " " + str("[Dataset]")
        year_publication_dataset_version = str(dataset_version.modified_date)[0:4]
        distributor = "FORS - Swiss Centre of Expertise in the Social Sciences"
        reference_number_dataset = dataset.reference_number
        data_version_dataset_version = dataset_version.data_version
        doi_dataset_version = dataset_version.doi
        data_type_dataset_version = "Dataset"
        abstract = study_version_translation[0].abstract.replace("\r\n", " ")

        citation_data = {}
        citation_data["language"] = dataset_language_translation
        citation_data["type_of_reference"] = "Dataset"
        citation_data["year"] = year_publication_dataset_version
        citation_data["title"] = dataset_title
        citation_data["publisher"] = distributor
        citation_data["edition"] = data_version_dataset_version
        citation_data["place_published"] = "Lausanne"
        citation_data["abstract"] = abstract
        citation_data["authors"] = investigator
        citation_data["custom3"] = data_type_dataset_version
        citation_data["custom4"] = "datasets"
        citation_data["access_date"] = datetime.now().strftime("%d-%m-%Y")
        citation_data["number_of_volumes"] = dataset.reference_number

        if doi_dataset_version:
            citation_data["doi"] = doi_dataset_version
            citation_data["url"] = "https://doi.org/" + doi_dataset_version
        else:
            citation_data["doi"] = ""
            citation_data["url"] = ""

        if dataset.bibliography_citation:
            citation = []
            citation.append("Bibliographical citation recommended by FORS in agreement with the dataset authors : " + dataset.bibliography_citation.replace("\r\n", " "))
            citation_data["notes"] = citation
        else:
            citation = []
            citation.append("")
            citation_data["notes"] = citation

        entries = [
             citation_data
            ]

        response = HttpResponse(content_type="application/x-research-info-systems")
        response["Content-Disposition"] = "attachment; filename=dataset_" + str(reference_number_dataset) + "_ris_export.ris"
        dump(entries, response)
        response.write("\ufeff")
        return response