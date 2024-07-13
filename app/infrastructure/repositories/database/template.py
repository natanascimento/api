from app.core.logging import logger
from app.domain.case.entities import TemplateCreationResponse

class RepositoryTemplate:

	@staticmethod
	def create(request):

		try:
			logger.info(f"Trying to create location {request.location}")
			return TemplateCreationResponse(location=request.location)
		except Exception as exception:
			return logger.error(exception)