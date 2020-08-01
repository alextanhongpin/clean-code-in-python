from .ex02_unittest import MergeRequest, MergeRequestStatus, MergeRequestException

def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("maintainer")
    assert merge_request.status == MergeRequestStatus.REJECTED

def test_juest-c


