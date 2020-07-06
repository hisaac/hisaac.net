# frozen_string_literal: true

module Jekyll
  # Simple filter to extract the hostname from a given URL
  module ExtractHostname
    def extract_hostname(input)
      URI.parse(input).host.sub(/\Awww\./, '')
    end
  end
end

Liquid::Template.register_filter(Jekyll::ExtractHostname)
