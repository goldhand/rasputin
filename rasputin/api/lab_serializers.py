from rest_framework import serializers
from reports.models import LabReport


class LabReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReport
        fields = ("id", "lab", "customer_id", "sample_name", "test_id", 
                  "sample_type", "batch", "test_date", "units", "test_date", 
                  "thc", "thc_a", "thc_v", "cbd", "cbd_a", "cbd_v", "cbc", 
                  "cbg", "cbn", "max_thc", "max_cbd", "total_active", 
                  "total_cannabinoids",)
        read_only_fields = ("lab",)
