from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import get_tracer, set_tracer_provider

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("yoda-logger")

# Set up OpenTelemetry TracerProvider
resource = Resource(attributes={"service.name": "yoda-service"})
tracer_provider = TracerProvider(resource=resource)
set_tracer_provider(tracer_provider)

# Set up OTLP exporter for traces
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")  # Ensure this matches the collector config
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

# Create a tracer
tracer = get_tracer(__name__)

# Start a trace and log with trace context
with tracer.start_as_current_span("yoda-log-span") as span:
    trace_id = span.get_span_context().trace_id
    span_id = span.get_span_context().span_id

    logger.info(
        "This is a Yoda-level log",
        extra={"trace_id": hex(trace_id), "span_id": hex(span_id)},
    )
