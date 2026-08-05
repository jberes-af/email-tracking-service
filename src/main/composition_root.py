# /src/main/composition_root.py

repository = GoogleSheetsEmailTrackingRepository()

track_open_use_case = TrackEmailOpenUseCase(
    repository,
)

track_click_use_case = TrackEmailClickUseCase(
    repository,
)
