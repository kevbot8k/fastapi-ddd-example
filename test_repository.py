import adapters.repository as repository, domain.model as model

def test_repository_can_save_a_batch():
    batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)

    repo = repository.FakeRepository()
    repo.add(batch)

    rows = repo.get(batch.reference)
    assert list(rows) == [("batch1", "RUSTY-SOAPDISH", 100, None)]