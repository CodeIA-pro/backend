from rest_framework import serializers
from codeia.models import Project, Asset

class ProjectAssetSerializer(serializers.ModelSerializer):
    subsection = serializers.SerializerMethodField()
    class Meta:
        model = Asset
        fields = ['id', 'version', 'titulo', 'description', 'more_description', 'depth', 'url', 
                  'is_father', 'father_id', 'subsection']
        read_only_fields = ['id', 'created_at']

    def get_subsection(self, obj):
        subsection_asset = obj.subsection.all().order_by('id')
        return ProjectAssetSerializer(subsection_asset, many=True).data

class ListProjectSerializer(serializers.ModelSerializer):
    assets = ProjectAssetSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'branch', 'url_repo', 'user_repo', 'latest_build', 
                  'last_version', 'assets']
        read_only_fields = ['id']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'branch', 'url_repo', 'user_repo', 'latest_build']
        read_only_fields = ['id']
    
class ChangeProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = []
        read_only_fields = ['id', 'title', 'branch', 'url_repo', 'user_repo', 'latest_build', 
                  'last_version']

# Error Serializer
class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()