class DataIngestionArtifact:

    def __init__(self, trained_file_path: str, test_file_path: str):
        self.trained_file_path = trained_file_path
        self.test_file_path = test_file_path

    def __repr__(self):
        return (
            f"DataIngestionArtifact("
            f"trained_file_path={self.trained_file_path}, "
            f"test_file_path={self.test_file_path})"
        )