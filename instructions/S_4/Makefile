# Auto-generated help menu: lists targets with comments
.PHONY: help
help:
	@echo "Available make commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*#' $(MAKEFILE_LIST) | \
	  sed -E 's/^([a-zA-Z0-9_-]+):.*# ?(.*)/\1|\2/' | \
	  awk -F'|' '{printf "  make %-22s %s\n", $$1, $$2}'

.PHONY: venv
venv:   # Create Python virtual environment if missing
	@if [ ! -d ".venv" ]; then \
		echo "Creating Python virtual environment..."; \
		python3 -m venv .venv; \
		echo "To activate, run: source .venv/bin/activate"; \
	else \
		echo "Python virtual environment already exists."; \
		echo "To activate, run: source .venv/bin/activate"; \
	fi

.PHONY: frontend
frontend:         # Start frontend
	cd frontend && npm run dev

.PHONY: install-dependencies
install-dependencies:   # Install backend & frontend dependencies
	find backend -name "requirements-dev.txt" -exec pip install -r {} \;
	cd frontend && npm install

.PHONY: start-backend-clean
start-backend-clean:    # Remove dev volume and rebuild backend
	podman volume rm local_dev_demo_backend_data || true
	podman compose up --build

.PHONY: start-backend
start-backend:          # Start backend (no rebuild)
	podman compose up

.PHONY: lint
lint: # Run Python linter
	flake8 backend

.PHONY: lint-frontend
lint-frontend: # Run frontend linter
	cd frontend && npm run lint

.PHONY: test
test: # Run Python tests with PYTHONPATH set
	PYTHONPATH=backend pytest backend/tests