import pytest
from pipeline import PipelineError, process_pipeline


def test_invalid_csv_payload(tmp_path):
    # إنشاء ملف ثنائي وهمي غير صالح لاختبار المعالجة
    invalid_file = tmp_path / "invalid.csv"
    invalid_file.write_bytes(b"\x00\x01\x02\x03\xff\xfe")

    with pytest.raises(PipelineError):
        process_pipeline(str(invalid_file))
